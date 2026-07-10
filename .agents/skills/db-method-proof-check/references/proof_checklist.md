# Proof Checklist

- assumptions explicit
- definitions introduced before theorem usage
- dependency chain closed
- learned/heuristic component separated from the exact correctness argument
- fallback, ties, empty inputs, duplicate keys, disconnected graphs, and degenerate bounds handled where relevant
- update invariant proves that the logical indexed set matches current state
- every excluded candidate group covered by a valid certificate or exact fallback
- complexity model and terms explicit
- main-text complexity reduced to the simplest meaningful asymptotic form
- detailed derivation does not silently add assumptions absent from the main statement
- claim-proof-evidence pointers complete

Full-path closure:
1. candidate generation cannot remove a valid answer without a certificate
2. verification computes the semantics in the problem definition
3. termination covers every unseen candidate or invokes exact fallback
4. updates preserve the logical active set seen by access and verification
5. pseudocode return values match the formal answer object and tie order
