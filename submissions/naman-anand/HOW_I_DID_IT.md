# HOW I DID IT - Level 2 (Track E)

**Contributor:** Naman Anand
**Track:** QA & Security

## Step-by-Step Methodology

1.  **Environment Setup:** I cloned the repository and initialized the environment using `npm install`. I encountered a small delay with dependencies due to network speed, so I used the `--prefer-offline` flag as suggested in the troubleshooting guide.
2.  **Validation:** Ran `npm run test-client` to ensure the baseline was stable. All 8/8 tests passed, confirming the MCP server logic was sound before I started manual testing.
3.  **Manual Fuzzing:** Instead of just running automated tests, I manually invoked the server using `node dist/src/index.js`. I focused on "Black Box" testing—sending inputs that the developers likely didn't expect, such as SQL injection strings (`DROP TABLE`), malformed JSON, and empty objects.
4.  **Information Gathering:** I analyzed the error outputs. I noticed that while the tools are read-only, the server's error handling reveals internal directory structures, which I documented as a security finding.

## Problems Encountered & Solutions

* **SSH Permission Issue:** Initially, I couldn't clone the repo via SSH (`Permission denied`). I realized my local SSH key wasn't linked to GitHub. I solved this by switching to the HTTPS protocol for a faster setup.
* **Server "Hanging":** When I sent non-JSON text, the server stopped responding. At first, I thought my terminal crashed, but I realized it was a protocol mismatch where the server waits indefinitely for a valid JSON-RPC frame.

## Lessons Learned

* **MCP Protocol:** I learned how Model Context Protocol (MCP) servers handle standard input/output (stdio) for agent communication.
* **SMILE Rigor:** I learned that Digital Twins require a "Reality Emulation" phase. From a security perspective, this taught me that understanding the current 'as-is' state of a system is the first step in protecting it.




