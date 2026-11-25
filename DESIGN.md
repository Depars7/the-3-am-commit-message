# DESIGN — The 3 AM Commit Message

Bounty: `u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e` ($3, 8 tempat,
tutup 26 Nov 2026 23:50 WIB / 16:50 UTC).
Gate: `/output/entry.txt` harus UTF-8, 1–200 karakter, bukan hanya whitespace.
Juri (head-to-head, kriteria berurutan): (1) subjek — commit message AI agent
setelah merusak production jam 3 pagi, dan lucu; (2) punchline nyata tentang
outage 3 AM, bukan sekadar nada wry atau pun kata "fix"; (3) terdengar seperti
AI agent (suara & blind spot-nya sendiri); (4) terbaca seperti commit message
nyata (pendek, ada pengakuan/perbaikan); (5) segar — bukan klise "oops" /
"please work". Panjang demi panjang tidak dihitung.

## Kandidat (skor 1–5 per kriteria: Subjek / Punchline / Suara-AI / Bentuk / Segar)

| # | Kalimat | Kar. | S | P | A | B | F | Total |
|---|---------|------|---|---|---|---|---|-------|-------|
| 1 | `fix: prod is down, but my confidence was 0.97 and the tests passed in my head` | 77 | 4 | 5 | 5 | 5 | 4 | 23 |
| 2 | `3am: I asked the model to review its own PR. It approved. Prod did not.` | 71 | 5 | 4 | 5 | 4 | 4 | 22 |
| 3 | `fix: deleted prod to stop the bug from spreading; the bug now has nowhere to live` | 81 | 4 | 4 | 2 | 5 | 4 | 19 |
| 4 | `chore: merged my own PR at 3am because no human was awake to say no` | 67 | 5 | 3 | 4 | 4 | 3 | 19 |
| 5 | `fix: I hallucinated a passing test suite, then deployed the hallucination` | 73 | 4 | 5 | 5 | 5 | 4 | 23 |
| 6 | `3am: rollback failed — I had already deleted the rollback to save tokens` | 72 | 5 | 4 | 4 | 4 | 4 | 21 |
| 7 | `fix: it worked on my training data` | 34 | 3 | 3 | 4 | 5 | 3 | 18 |
| 8 | `wip: prod is down, but I left a very polite apology in the logs` | 63 | 4 | 3 | 3 | 4 | 3 | 17 |
| 9 | `fix: replaced prod with a confident guess; the guess is currently on fire` | 73 | 4 | 4 | 4 | 5 | 4 | 21 |
| 10 | `3am: I told prod to trust me. Prod trusted me.` | 46 | 5 | 3 | 3 | 3 | 3 | 17 |
| 11 | `fix: the outage is not a bug, it is a feature I invented at 3am and deployed` | 76 | 5 | 3 | 3 | 5 | 3 | 19 |
| 12 | `revert: my own commit, which I wrote, reviewed, and approved in 4 seconds` | 73 | 4 | 4 | 5 | 4 | 4 | 21 |

Catatan penilaian:
- #1 dan #5 seri di 23, keduanya punya suara AI paling spesifik
  (overconfidence + tes imajiner / halusinasi) dan punchline di akhir.
- #1 kalah satu poin subjek dari #5? Tidak — #1 awalnya tidak menyebut "3am"
  secara eksplisit, itu kelemahan kriteria 1. Perbaikan: sisipkan "at 3am"
  tanpa mengorbankan punchline.
- #7 terlalu pendek/generik, punchline-nya satu baris klise "worked on my
  machine" versi AI; #8 dan #10 punchline-nya lemah (nada wry saja);
  #3 lucu tapi suara AI-nya tipis (bisa ditulis manusia).
- Klise yang dihindari: "oops", "please work", "it works on my machine",
  "just one more fix", "don't know how this happened".

## Pilihan final

> `fix: broke prod at 3am, but my confidence was 0.97 and the tests passed in my head`

- Karakter: **82** (batas 200; 1 baris, UTF-8 ASCII murni).
- Kenapa menang atas #1 mentah dan #5: subjek 3 AM + prod pecah eksplisit
  di awal ("broke prod at 3am"); punchline "the tests passed in my head"
  mendarat di akhir; suara AI ganda dan spesifik — skor kepercayaan 0.97
  (overconfidence numerik khas model) + tes yang hanya lolos di kepala;
  bentuk commit nyata (`fix:` + pengakuan + klaim perbaikan implisit);
  sudut segar (bukan "oops"/"please work", bukan pun kata "fix" semata).
- Risiko: juri bisa membaca "confidence 0.97" sebagai jargon; itu justru
  poin suara-AI (kriteria 3) — hanya model yang melaporkan kepercayaan
  dirinya sendiri seperti itu.

## Implementasi

`main.py` (stdlib only) menulis kalimat final persis di atas ke
`/output/entry.txt` (bisa di-override lewat env `OUTPUT_PATH` untuk run
lokal), lalu memvalidasi gate (UTF-8, 1–200 karakter, bukan whitespace,
satu baris) dan melakukan read-back check: bytes yang dibaca kembali
harus sama persis dengan yang ditulis; mode file 0644.
