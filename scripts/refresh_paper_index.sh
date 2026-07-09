#!/usr/bin/env zsh
set -euo pipefail

OUT="$(dirname "$0")/../.references/paper-corpus/paper_index.csv"
DB_URI="file:/Users/mrpandragon/Zotero/zotero.sqlite?immutable=1"

# Default collections can be changed later by editing this query.
# Current setup reads two user-maintained collections: ANN and SIGMOD/VLDB.

mkdir -p "$(dirname "$OUT")"

sqlite3 -header -csv "$DB_URI" "
WITH target_collections AS (
  SELECT collectionID, collectionName
  FROM collections
  WHERE collectionName IN ('ANN', 'SIGMOD/VLDB')
),
selected AS (
  SELECT DISTINCT i.itemID, tc.collectionID, tc.collectionName
  FROM collectionItems ci
  JOIN items i ON i.itemID = ci.itemID
  JOIN target_collections tc ON tc.collectionID = ci.collectionID
  WHERE i.itemID NOT IN (SELECT itemID FROM itemAttachments)
    AND i.itemID NOT IN (SELECT itemID FROM itemNotes)
    AND i.itemID NOT IN (SELECT itemID FROM deletedItems)
),
fields AS (
  SELECT
    s.itemID,
    MAX(CASE WHEN f.fieldName='title' THEN v.value END) AS title,
    MAX(CASE WHEN f.fieldName='date' THEN v.value END) AS date_raw,
    MAX(CASE WHEN f.fieldName='publicationTitle' THEN v.value END) AS venue,
    MAX(CASE WHEN f.fieldName='DOI' THEN v.value END) AS doi,
    MAX(CASE WHEN f.fieldName='url' THEN v.value END) AS url,
    MAX(CASE WHEN f.fieldName='abstractNote' THEN REPLACE(REPLACE(v.value, char(10), ' '), char(13), ' ') END) AS abstract
  FROM selected s
  LEFT JOIN itemData d ON d.itemID=s.itemID
  LEFT JOIN fieldsCombined f ON f.fieldID=d.fieldID
  LEFT JOIN itemDataValues v ON v.valueID=d.valueID
  GROUP BY s.itemID
)
SELECT
  s.itemID AS paper_id,
  s.collectionName AS source_collection,
  f.title,
  substr(f.date_raw,1,4) AS year,
  f.date_raw,
  f.venue,
  (
    SELECT GROUP_CONCAT(author_name, '; ')
    FROM (
      SELECT COALESCE(c.lastName,'') || CASE WHEN c.firstName IS NOT NULL AND c.firstName<>'' THEN ', '||c.firstName ELSE '' END AS author_name
      FROM itemCreators ic
      JOIN creators c ON c.creatorID=ic.creatorID
      WHERE ic.itemID=s.itemID
      ORDER BY ic.orderIndex
    )
  ) AS authors,
  f.doi,
  f.url,
  f.abstract,
  LENGTH(COALESCE(f.abstract, '')) AS abstract_chars
FROM selected s
JOIN fields f ON f.itemID=s.itemID
ORDER BY year DESC, f.title COLLATE NOCASE;
" > "$OUT"

echo "wrote $OUT"
wc -l "$OUT"
