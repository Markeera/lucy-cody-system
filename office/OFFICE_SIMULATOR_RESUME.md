# OFFICE SIMULATOR — standalone resume checkpoint
Updated 2026-11-25 11:21 ICT (Asia/Bangkok). User explicitly wants a clean new chat to turn this into a real Office Simulator. Status: pending continuation, not complete. Scope: Office only; do not touch V6 production, n8n, VoiceStudio or original production Dashboard.

## Load order
1. Global rules: https://github.com/Markeera/Lucy-Edit-Kit/blob/main/bootstrap/MASTER_OPERATING_RULES_V2.md
2. This file, then office/2026-11-25-live-runtime-handoff.md (latest entry first; older entries historical).
3. Current office/runtime/index.html and server.py, rig asset files referenced below. Check current runtime and Desktop Commander before editing. Do not restart old rejected experiments.

## Current baseline
Latest recorded implementation: Living Office jointed sprite prototype v1, not v0.9.1. Current HTML blob 93fff7545bab22e0c01aa98216f20719f15b9d5b at checkpoint. Separate head, torso, arms, legs from six actual character sheets; independent idle timing and walking, cat paw movement. Original office sign, boards, desk labels, floor and laptop art retained; wall/chairs reconstructed. Local Chromium rendered two distinct frames and walking state, no JS errors. Remote HTTPS endpoints /, /rig.js, /rig-atlas.png, /api/state returned HTTP200 in prior verification; live visual acceptance remains pending. Cutout-style motion, basic gestures, background seams and cat artifacts remain. This is a prototype, not final acceptance.
- Runtime HTML commit 01bd48aaf2ff4078f6fb8184df3707f322f825f6; server commit 00837c7d279dea03497d337d249c0562a93a6c6e.
- Rig JS base64 commit 632b1663e01c7d5a423d1c929b57fede24b81e70; decoded SHA256 58d9335036acd305d6b68db026aca8e1695c3a1d837d5a392d2966e436a80f4d (6175 bytes).
- Atlas: office/assets/rig-atlas.part0.b64 + part1.b64 concatenate then decode; SHA256 d302d88c6657154487b933ba6da8347bf2109c64fb2b5bd7300d22ac47501728 (443956 bytes).
- Original artwork restore: office/assets/RESTORE_MANIFEST.json. Older pose atlas manifests are historical.
- PC runtime: E:\LucyRun\projects\office-simulator; local http://127.0.0.1:8766/; private https://desktop-3kcjp1m.tailbed451.ts.net:8443/ (Tailscale required). Server previously stopped, restored 10:11 ICT; automatic startup not yet configured. GitHub canonical, PC execution host only.

## User acceptance criteria / next work
Actual independent character animation, not parallax, image warping, popups, or crossfading static poses. All five agents (Script, Voice, Lucy, Visual, Editing) and cat retain approved identity; independent continuous role-appropriate idle actions even without work, walking and believable transitions; cat sleeps, stretches and walks. Entire office fits one viewport without scrolling. Preserve approved art direction and existing live status integration. Evolve into a real simulator with explicit agent states, activities, transitions and actual job-linked behavior; do not misrepresent decorative simulation as real agent work. Implementation details for orchestration are not yet approved/complete. First inspect actual prototype, then improve independent animation and scene composition; verify live browser frames, real idle and work states, no duplicated characters or artifacts, and preserve existing services. Reuse existing Chrome tab and Desktop Commander. No unapproved costs or destructive changes. Save meaningful progress and evidence in GitHub; deliver working simulator link only after verified result or genuine blocker. No background work promised after turn.
