# 13-Exceptions

Facts are sourced per record; **Editorial view** lines are CounselMode judgments (not legal advice).

## Linux syscall note — `Linux-syscall-note`

- **base:** GPL-2.0-only
- **effect:** User-space programs calling the kernel through normal system calls are not "derived works" of the kernel
- notable_projects: Linux kernel (UAPI headers)
- notes: Apps on Linux can be under any license; kernel modules not covered.
- **Editorial view – practical_effect:** Apps on Linux can be under any license; kernel modules not covered.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## Classpath exception 2.0 — `Classpath-exception-2.0`

- **base:** GPL-2.0-only
- **effect:** Linking independent modules with the library does not extend the GPL to them
- notable_projects: OpenJDK, GNU Classpath
- notes: Java apps on OpenJDK can be any license; modifying the JDK itself is GPL.
- **Editorial view – practical_effect:** Java apps on OpenJDK can be any license; modifying the JDK itself is GPL.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## GCC Runtime Library exception 3.1 — `GCC-exception-3.1`

- **base:** GPL-3.0-or-later
- **effect:** Programs compiled with GCC through an "Eligible Compilation Process" may combine runtime libraries under any license
- notable_projects: libgcc, libstdc++
- notes: Compiled programs unaffected.
- **Editorial view – practical_effect:** Compiled programs unaffected.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## LLVM exception — `LLVM-exception`

- **base:** Apache-2.0
- **effect:** Waives Apache-2.0 sections 4(a), 4(b) and 4(d) for portions compiled into your object code; for software combined with GPLv2 code, Apache terms may be deemed waived only if a court finds a conflict
- notable_projects: LLVM, Clang, libc++
- notes: Very permissive. Not unconditionally GPLv2-compatible: the GPLv2 clause is a conditional waiver.
- **Editorial view – practical_effect:** Very permissive; GPLv2-compatible.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## OpenSSL linking exception — `Note-OpenSSL-linking-exception`

- **base:** GPL-2.0 / GPL-3.0
- **effect:** Permits linking GPL code with OpenSSL 1.x (whose old license was GPL-incompatible)
- **triggers:** ['distribution']
- **obligations:** ['source_disclosure']
- notable_projects: wget, older GPL network tools
- notes: Less relevant since OpenSSL 3.0 moved to Apache-2.0 (GPLv3-compatible; still GPLv2-incompatible).
- **Editorial view – practical_effect:** Less relevant since OpenSSL 3.0 moved to Apache-2.0 (GPLv3-compatible; still GPLv2-incompatible).
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Note only - not an SPDX expression | last_verified: 2026-11-18 | volatile: False

## Autoconf exception 3.0 — `Autoconf-exception-3.0`

- **base:** GPL-3.0-or-later
- **effect:** Generated configure scripts may be distributed under any license
- notable_projects: Autoconf
- notes: configure scripts in your package do not make it GPL.
- **Editorial view – practical_effect:** configure scripts in your package do not make it GPL.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## Bison exception 2.2 — `Bison-exception-2.2`

- **base:** GPL-2.0-or-later / GPL-3.0
- **effect:** Parser skeleton code output by Bison may be used under any license
- notable_projects: GNU Bison
- notes: Generated parsers are free to use.
- **Editorial view – practical_effect:** Generated parsers are free to use.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## Font exception 2.0 — `Font-exception-2.0`

- **base:** GPL
- **effect:** Embedding a GPL font in a document does not make the document GPL
- notable_projects: GNU FreeFont
- notes: Documents with embedded fonts unaffected.
- **Editorial view – practical_effect:** Documents with embedded fonts unaffected.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## Universal FOSS exception 1.0 — `Universal-FOSS-exception-1.0`

- **base:** GPL-2.0-only
- **effect:** Allows combination with code under any OSI-approved/FSF-free license without GPL extending to it
- notable_projects: Oracle MySQL Connectors
- notes: Eases combining connectors with OSS apps (not proprietary).
- **Editorial view – practical_effect:** Eases combining connectors with OSS apps (not proprietary).
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-18 | volatile: False

## MySQL FOSS License Exception — `AdditionRef-MySQL-FOSS-exception`

- **base:** GPL-2.0-only
- **effect:** Earlier Oracle exception for FOSS applications using MySQL client libraries
- **triggers:** ['distribution']
- **obligations:** ['source_disclosure']
- notable_projects: Older MySQL client libraries
- notes: Proprietary distribution still requires commercial license.
- **Editorial view – practical_effect:** Proprietary distribution still requires commercial license.
- provenance: https://spdx.org/licenses/exceptions-index.html (SPDX 3.29.0) | verification: Not on SPDX exceptions list - AdditionRef | last_verified: 2026-11-18 | volatile: False

## Swift Exception (Runtime Library Exception to Apache-2.0) — `Swift-exception`

- **base:** Apache-2.0
- **effect:** If you compile your source code with the Software and portions of it end up embedded in the binary product, you may redistribute that product without the attribution Apache-2.0 sections 4(a), 4(b) and 4(d) would otherwise require
- notable_projects: Swift (swiftlang/swift), Swift Package Manager
- notes: Applies only to portions embedded in your binary by compiling with Swift; redistributing the Swift toolchain itself still needs full Apache-2.0 compliance.
- **Editorial view – practical_effect:** Apps compiled with Swift do not need Apache-2.0 notices for the runtime code embedded in them; the toolchain itself stays under Apache-2.0.
- provenance: https://github.com/swiftlang/swift/blob/swift-6.4.3-RELEASE/LICENSE.txt ; https://github.com/swiftlang/swift-package-manager/blob/swift-6.4.3-RELEASE/LICENSE.txt ; https://spdx.org/licenses/Swift-exception.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-23 | volatile: False

## Qt LGPL exception 1.1 (The Qt Company Qt LGPL Exception version 1.1) — `Qt-LGPL-exception-1.1`

- **base:** LGPL-2.1-only
- **effect:** Object code of a "work that uses the Library" may include material from unmodified Qt header files (numerical parameters, data structure layouts, accessors, macros, inline functions and templates) and be distributed on terms of your choice, if you still comply with LGPL-2.1 section 6
- **triggers:** ['distribution']
- **obligations:** ['relinking']
- notable_projects: Qt 5 (qtbase) LGPL-2.1 offer, Qt 5.5 to 5.6 (this wording); Qt 5.4.x carries the "Digia Qt LGPL Exception version 1.1" wording instead
- notes: Qt source file headers at v5.6.3 offer LGPL-2.1 or LGPL-3.0 and point to this exception. At v5.7.0 the same headers offer LGPL-3.0, GPL-2.0 or GPL-3.0 with no exception. The exception does not lift the LGPL-2.1 section 6 duties.
- **Editorial view – practical_effect:** Using Qt 5.6 or earlier under LGPL-2.1 does not make your object code a derivative of Qt just because it inlines Qt header material; you still owe the LGPL-2.1 section 6 duties, including letting users relink.
- provenance: https://github.com/qt/qtbase/blob/v5.6.3/LGPL_EXCEPTION.txt ; https://github.com/qt/qtbase/blob/v5.6.3/src/corelib/global/qglobal.cpp ; https://github.com/qt/qtbase/blob/v5.7.0/src/corelib/global/qglobal.cpp ; https://github.com/qt/qtbase/blob/v5.4.0/LGPL_EXCEPTION.txt ; https://spdx.org/licenses/Qt-LGPL-exception-1.1.html (SPDX 3.29.0) | verification: Verified (primary) - on SPDX 3.29.0 exceptions list | last_verified: 2026-11-23 | volatile: False

