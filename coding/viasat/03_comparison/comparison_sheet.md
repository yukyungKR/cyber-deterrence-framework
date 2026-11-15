---
title: "Viasat KA-SAT(2022) 회차 2 두 모델 코딩 대조 시트"
type: sheet
status: draft
tags: [cases, viasat, 회차2]
created: 2026-10-13
updated: 2026-10-13
---

> 묶음 `pack_r2/` 23건을 Claude(Opus)·Claude(Fable)가 회차 1 산출을 보지 않고 독립 코딩했다(지시문 `00_코딩지시문_회차2_viasat.md` · 격리 사본). 이 시트는 ⓐ 회차 2 두 코더의 필드별 대조와 ⓑ 회차 1 확정 레코드 대비 바뀐 키를 기계로 집계한다. 어느 값이 맞는지 고르지 않는다 — 「저자 확정」 칸은 저자가 채운다.
> 이 시트는 보조 스크립트가 만든다(생성 시각을 적지 않는다 — 같은 입력이면 재실행 바이트가 같다). 판정 규칙은 스크립트 docstring.
> 입력 sha256: `coding_r2_claude_opus.json` `bbc2d4d24539b39cb6cedffe48e2de95ebf81629615d078c54cac92982649920` (배정 값과 같음) · `coding_r2_claude_opus_근거.md` `fff2f616e52f9ddb9eaf602ab6827fb3d7bf95422c12e118886dd54a71a40eb1` (배정 값과 같음) · `coding_r2_claude_fable.json` `9b8f287da84659e904d40127cde979a55b1ba101b42f2034c4a73f43255059bb` (배정 값과 같음) · `coding_r2_claude_fable_근거.md` `b57502ccadb9241fb04f0cdcf8d4f19e1b16962181ce335c3ba8533ca426461c` (배정 값과 같음) · Fable 재작업 전 판(재작업 1회 전 · 대조 입력 아님) JSON `b7c88ab94de0acbd0b3ae250b687dc3d245563547c2f1a5a546a04dc5ca06d99` · 근거 md `aa9446c41691908df771105978e8b5f8a128767af74138c1fae9a9d6edea24bc`.
> `coding_r2_claude_opus.json`의 원 산출은 CRLF(`bbc2d4d24539b39cb6cedffe48e2de95ebf81629615d078c54cac92982649920`)이고, 대조 입력은 LF로 정규화한 사본(sha256 `e20e66cc36d4333e675351007c8daaa01d8bccba207da243491e5c510d35e7f9`)이다.
> **코딩 검증** — Opus 합격 · Fable 불합격 → 기계적 2건(M-1 인용 줄 범위 · M-2 대응 근거 문면의 날짜) 재작업 1회(값 불변) → 차분 검증 합격(새 결함 0 · 값 불변 · §5) · 판단 사안은 V-1~V-4.
> 회차 1 정본 확정값 = 회차 1 확정 레코드(sha256 `663e6d2400ef9fced26fee5d2a33fabeee3fb349b2fecd13d9e5d8a191e6dea5` · 34키 전부 · 회차 1 두 코더 산출과 회차 1 저자 확정에서 만든 레코드). 회차 1 저자 확정(sha256 `d59182e4e2fc30978a3f90e8dd3b241ae2af137e95d96a32ad0a196569d4eaff`)은 저자 결정 원천(decisions 9건)이지 레코드 전체가 아니다 — 결정값이 확정 레코드와 9/9 같고, meta `annotation_pass`도 같다.
> **머리 사실** — 두 코더 모델: Opus `claude-opus-5-5` · Fable `claude-fable-5-1` · 분류기 정지(검증 보고 값): Opus 0 · Fable 0(재작업 전 세션) · Fable 재작업 세션 0(재작업 차분 검증 합격(§5)) · 격리 빌드 넷째 판(목록 해시 `418b4a72…`) · 양식 §A 발췌 가림 M1~M7(여섯 줄) · S13(`none_observed`의 `source` = `manifest_min.json` · 지시문 사본 76행) · 묶음 23건(`pack_r2/manifest.json` items).
> **V-1** 양식 §A 개정 ⑵가 정본 — 첫 값 = 주 표적 규칙으로 저자 확정 · 회차 2 지시문 §3 :64 「1값」 문면은 다음 손질 때 정정.
> **V-2** Fable 셸 `||` 1회 · 열람 순서(22 ↔ 23) — 저자 판단 사안(사전 선언 규칙 위반 의심 · 효과 없음) · 이 시트의 값은 원 산출 그대로.
> **V-4** `annotation_pass`는 대조 키에서 뺀다(메타). CRLF → LF 정규화(대조 입력 사본에만 · 원 산출 보존): `coding_r2_claude_opus.json` 231.
> **치환**(대조 사본에만 · 두 코더 똑같이): `c_st.reference_date` `"none"` → 「공식성명 부재」 Opus 0 · Fable 0 · S13 `none_observed` `source` 맞춤 Opus 0 · Fable 0 · 회차 1 확정 0. 그 밖의 치환 없음. 같은 꼴(`by_type` `pre` + 근거 칸 「묶음에 근거 없음」 — 치환하지 않음): Opus 0 · Fable 0.
> **줄 보완**(값 안 「 」 인용에 파일:줄 없음 · 부록 A): Opus 6곳(보완 2 · 줄 미상 4) · Fable 7곳(보완 5 · 줄 미상 2).
> 두 코더 일치 21 가운데 7은 코딩하지 않은 칸이다(템플릿 선기입 5 — `case_id` · `tier` · `collection_mode` · `collection_mode_basis` · `identified_date` / 두 코더 모두 빈 메타 키 2 — `terminal_objective` · `countermeasure_availability`) — 독립 코딩 값이 일치한 칸은 14다.
> 형식 · 원문 열람 증명 · 근거 구절 원문 대조 · 세션 감사는 코딩 검증 보고가 했다(이 시트는 다시 하지 않는다).
> **저자 확정 기입**(2026-10-14 · 저자가 44필드를 선택해 확정 · 에이전트 후보·추천 없음). 「Fable r2 문구 그대로」 = 부록 B의 Fable r2 칸 전문. 일치 칸은 저자가 개별 확인. V-1(첫 값 = 주 표적) 적용: victim_sector 첫 값 ict, victim_sector_sub 첫 값 communications. 값끼리 어긋남을 안내받고 유지한 곳: #7 c_id.source(Opus 4개 파일) ↔ #6 근거 문구(Fable).

## 0. 한눈에

- 비교 필드 44(템플릿 45항목 − `annotation_pass`).
- ⓐ 회차 2 두 코더: 일치 21 · 서술 차이 13 · 값 불일치 10 · 한쪽 결측 0.
- ⓑ 회차 1 확정 ↔ Opus: 일치 21 · 서술 차이 14 · 값 불일치 9 · 한쪽 결측 0 / 회차 1 확정 ↔ Fable: 일치 20 · 서술 차이 14 · 값 불일치 10 · 한쪽 결측 0.
- 회차 1 대비 바뀐 키: **값 바뀜 11**(두 코더 모두 8 · Opus만 1 · Fable만 2) · 서술만 바뀜 14(두 코더 모두 14 · Opus만 0 · Fable만 0) · 같음 19.
- 값 바뀜 키: `alias`(두 코더 모두) · `actor`(Opus만) · `c_id.grade`(Fable만) · `c_id.source`(두 코더 모두) · `c_st.source`(두 코더 모두) · `victim_sector`(두 코더 모두) · `victim_state`(Fable만) · `techniques`(두 코더 모두) · `legal_characterization`(두 코더 모두) · `responses`(두 코더 모두) · `victim_sector_sub`(두 코더 모두)
- ⓐ 일치가 아닌 필드: `name`(서술 차이) · `alias`(값 불일치) · `actor`(값 불일치) · `c_id.grade`(값 불일치) · `c_id.basis`(서술 차이) · `c_id.source`(값 불일치) · `c_st.basis`(서술 차이) · `c_st.source`(값 불일치) · `victim_sector`(값 불일치) · `victim_state`(값 불일치) · `techniques`(값 불일치) · `access_depth.basis`(서술 차이) · `effect_realized.note`(서술 차이) · `effect_realized.time_basis`(서술 차이) · `intrusion_state.basis`(서술 차이) · `legal_characterization`(값 불일치) · `responses`(값 불일치) · `aftermath`(서술 차이) · `boundary_reason`(서술 차이) · `notes`(서술 차이) · `target_specificity_basis`(서술 차이) · `victim_sector_sub_note`(서술 차이) · `victim_assets`(서술 차이)

## 1. 필드별 대조 — 44필드(템플릿 순서 · 「저자 확정」은 저자가 채운다)

> 값 칸은 앞부분만(전체 값은 부록 B). 근거 칸 = 근거 md §1 행 수 · 첫 행 근거 md 줄 · 그 행 파일:줄 칸. 「값 안 인용 줄 보완」은 ④ 기계 보완(부록 A).

| # | 필드 | Opus r2 | Fable r2 | 판정 | 근거(Opus) | 근거(Fable) | 회차 1 확정값 | 저자 확정 |
|---|---|---|---|---|---|---|---|---|
| 1 | `case_id` | VIASAT-2022 | VIASAT-2022 | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | VIASAT-2022 | VIASAT-2022 (일치 · 그대로) |
| 2 | `name` (자유 서술) | Viasat KA-SAT 위성망 사이버 공격(2022) | Viasat KA-SAT 위성 광대역망 공격(2022) | 서술 차이 | 1행 · 근거.md:39 · 11_viasat_2022-03-30.txt:24; 01_eurepoc_1514.txt:2 | 1행 · 근거.md:50 · 11_viasat_2022-03-30.txt:36 | Viasat KA-SAT 망 공격(2022) | 회차 1 확정 문구: Viasat KA-SAT 망 공격(2022) |
| 3 | `alias` | GRU, Main Directorate of the General Staff of the Armed Forces of the Russian Federation, Russian Military Intelligence | EuRepoC incident 1514, Viasat hack, KA-SAT Network cyber attack, AcidRain, ukrop, GRU, Main Directorate of the General Staff of t… | 값 불일치 — 공통 2 · Opus만 1 · Fable만 5 | 3행 · 근거.md:40 · 22_orkl_572fe6bb.txt:364 | 6행 · 근거.md:51 · 01_eurepoc_1514.txt:1 | EuRepoC 1514, Viasat Hack, KA-SAT 공격, AcidRain, ukrop, Russian Military Intelligence | 합집합 8개: EuRepoC incident 1514 / Viasat hack / KA-SAT Network cyber attack / AcidRain / ukrop / GRU / Main Directorate of the General Staff of the Armed Forces of the Russian Federation / Russian Military Intelligence |
| 4 | `actor` | GRU | Russian Military Intelligence | 값 불일치 | 1행 · 근거.md:43 · 22_orkl_572fe6bb.txt:363-364; 22_orkl_572fe6bb.txt:375 | 1행 · 근거.md:57 · 01_eurepoc_1514.txt:2 · 01_eurepoc_1514.txt:16-17 | Russian Military Intelligence | GRU |
| 5 | `c_id.grade` | 1 | 2 | 값 불일치 | 1행 · 근거.md:44 · 20_orkl_5ad57873.txt:98-99; 16_s1_acidrain_2022-03-31.txt:42 | 1행 · 근거.md:58 · 04_orkl_a097c1ac.txt:29-32 | 1 | 2 |
| 6 | `c_id.basis` (자유 서술) | 식별 시점(2022-02-24) 등급 1 — 식별 시점에 이 작전을 특정 행위자 집단에 연결한 서술이 묶음에 없다. 「ViaSat quickly suspected that disruptions could be the result o… | 식별 시점(2022-02-24) 기준 등급 2(추정 보도 수준). 식별 당일 묶음에는 행위자를 지목한 문서가 없고, 사후 서술이 당시의 추정만 전한다 — 「The timing coincided with the Russian inva… | 서술 차이 | 1행 · 근거.md:45 · 22_orkl_572fe6bb.txt:2521-2522; 14_uk_ncsc_2022-05-10.txt:39; 22_orkl… · 값 안 인용 줄 보완: 「perpetrated」 → 22_orkl_572fe6bb.txt:364 (줄 보완 — 기계) | 1행 · 근거.md:59 · 04_orkl_a097c1ac.txt:13-14 · 14_uk_ncsc_2022-05-10.txt:39 · 22_orkl_5… | 식별 시점(2022-02-24) 기준: 묶음 안에 이 시점의 행위자 식별 서술이 없다 — Viasat 개요는 「high volumes of focused, malicious traffic were detected」(11:46)와 「… | Fable r2 문구 그대로(부록 B) |
| 7 | `c_id.source` | 20_orkl_5ad57873.txt; 16_s1_acidrain_2022-03-31.txt; 22_orkl_572fe6bb.txt; 14_uk_ncsc_2022-05-10.txt | 04_orkl_a097c1ac.txt:29-32 | 값 불일치 — 가리키는 파일 다름 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | 11_viasat_2022-03-30.txt; 01_eurepoc_1514.txt; 04_orkl_a097c1ac.txt; 14_uk_ncsc_2022-05-10.txt; 13_us_state_2022-05-10.txt; 12_eu… | Opus r2 값 4개 파일 유지: 20_orkl_5ad57873.txt; 16_s1_acidrain_2022-03-31.txt; 22_orkl_572fe6bb.txt; 14_uk_ncsc_2022-05-10.txt (근거 문구 #6 Fable 문구와 인용 파일이 어긋남을 안내받고 유지 선택) |
| 8 | `state_attribution` | 러시아 | 러시아 | 일치 | 1행 · 근거.md:46 · 12_eu_hr_2022-05-10.txt:110; 14_uk_ncsc_2022-05-10.txt:39 | 1행 · 근거.md:60 · 12_eu_hr_2022-05-10.txt:110 | 러시아 | 러시아 (일치 · 그대로) |
| 9 | `c_st.grade` | 4 | 4 | 일치 | 1행 · 근거.md:47 · 12_eu_hr_2022-05-10.txt:110; 13_us_state_2022-05-10.txt:57; 14_uk_ncs… | 1행 · 근거.md:62 · 12_eu_hr_2022-05-10.txt:110 · 13_us_state_2022-05-10.txt:57 · 14_uk_n… | 4 | 4 (일치 · 그대로) |
| 10 | `c_st.basis` (자유 서술) | 귀속 기준일(2022-05-10 · 첫 공식 귀속 성명일) 등급 4 — 국가(러시아)를 수행 주체로 단정하나 국가기관(소속)은 특정하지 않는다(등급 5 「국가기관 소속 특정」 미충족). 「The European Union and i… | 귀속 기준일(2022-05-10 · 첫 공식 귀속 성명일) 기준 등급 4 — 국가(러시아 연방)의 행위라고 단정하되 국가기관(조직)은 특정하지 않음. EU 「strongly condemn the malicious cyber acti… | 서술 차이 | 1행 · 근거.md:50 · 22_orkl_572fe6bb.txt:2521-2522 · 값 안 인용 줄 보완: 「국가기관 소속 특정」 줄 미상(미발견) | 1행 · 근거.md:64 · 01_eurepoc_1514.txt:2 · 01_eurepoc_1514.txt:67 · 22_orkl_572fe6bb.txt… | 식별 시점(2022-02-24) 기준 등급 1: 묶음 안에 이 시점의 국가 귀속 서술이 없다(Viasat 개요는 「an attacker」(11:54), EuRepoC initiator_name 「Unknown」(01:16)). 20… | Fable r2 문구 그대로(부록 B) |
| 11 | `c_st.source` | 12_eu_hr_2022-05-10.txt; 13_us_state_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt; 20_orkl_5ad57873.txt | 12_eu_hr_2022-05-10.txt:110; 13_us_state_2022-05-10.txt:57; 14_uk_ncsc_2022-05-10.txt:39; 15_uk_fcdo_2022-05-10.txt:48 | 값 불일치 — 가리키는 파일 다름 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | 11_viasat_2022-03-30.txt; 01_eurepoc_1514.txt; 12_eu_hr_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt; 13_us_state_2022-05-10.txt; 15… | Fable r2 값 그대로: 12_eu_hr_2022-05-10.txt:110; 13_us_state_2022-05-10.txt:57; 14_uk_ncsc_2022-05-10.txt:39; 15_uk_fcdo_2022-05-10.txt:48 |
| 12 | `c_st.reference_date` | 2022-05-10 | 2022-05-10 | 일치 | 1행 · 근거.md:49 · 12_eu_hr_2022-05-10.txt:104; 12_eu_hr_2022-05-10.txt:110; 13_us_state… | 1행 · 근거.md:61 · 12_eu_hr_2022-05-10.txt:104, 110 · 13_us_state_2022-05-10.txt:53 · 14… | 2022-05-10 | 2022-05-10 (일치 · 그대로) |
| 13 | `victim_sector` | ict, critical_infrastructure | critical_infrastructure | 값 불일치 — 공통 1 · Opus만 1 · Fable만 0 | 2행 · 근거.md:51 · 11_viasat_2022-03-30.txt:36 | 1행 · 근거.md:65 · 01_eurepoc_1514.txt:14 | ict | [ict, critical_infrastructure] (첫 값 ict = 주 표적) |
| 14 | `victim_state` | 우크라이나 | 우크라이나(주 피해국) · 독일 · 폴란드 · 헝가리 · 그리스 · 이탈리아 · 프랑스(파급 피해국) | 값 불일치 | 1행 · 근거.md:56 · 11_viasat_2022-03-30.txt:36; 11_viasat_2022-03-30.txt:52 | 1행 · 근거.md:66 · 11_viasat_2022-03-30.txt:36 · 01_eurepoc_1514.txt:11 | 우크라이나 | 우크라이나 |
| 15 | `techniques` | T1190, T1133, T1072, T1498.001, T1083, T1485, T1561.001, T1495, T1529 | T1498, T1190, T1133, T1072, T1485, T1561.001, T1495, T1529, T1083 | 값 불일치 — 공통 8 · Opus만 1 · Fable만 1 | §2 기법 행 9 · 첫 행 근거.md:110 · §1 행 9(근거.md:57) | §2 기법 행 9 · 첫 행 근거.md:115 · §1 행 1(근거.md:67) | T1498.001, T1133, T1072, T1485, T1561.001, T1529 | Fable r2 9개: T1498, T1190, T1133, T1072, T1485, T1561.001, T1495, T1529, T1083 |
| 16 | `terminal_objective` | (빈 객체 {}) | (빈 객체 {}) | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | (빈 객체 {}) | {} (빈 객체 · 그대로) |
| 17 | `access_depth.draft` | core | core | 일치 | 1행 · 근거.md:66 · 11_viasat_2022-03-30.txt:54 | 1행 · 근거.md:68 · 11_viasat_2022-03-30.txt:54 | core | core (일치 · 그대로) |
| 18 | `access_depth.basis` (자유 서술) | 한 침투 안의 최댓값 = 운영자 망의 신뢰 관리 구간(특권 자산). 「Subsequent investigation and forensic analysis identified a ground-based network intrusion… | 공격자가 VPN 장비의 설정 오류를 통해 KA-SAT 망의 신뢰된 관리 세그먼트에 원격 접근하고, 망을 관리·운영하는 특정 네트워크 세그먼트까지 횡적 이동한 뒤 그 접근으로 다수 모뎀에 관리 명령을 실행했다 — 망 운영·관리 세그먼… | 서술 차이 | 1행 · 근거.md:67 · 11_viasat_2022-03-30.txt:54; 11_viasat_2022-03-30.txt:40 | 1행 · 근거.md:69 · 11_viasat_2022-03-30.txt:40 · 04_orkl_a097c1ac.txt:28-29 | 「Subsequent investigation and forensic analysis identified a ground-based network intrusion by an attacker exploiting a misconfig… | Fable r2 문구 그대로(부록 B) |
| 19 | `timing_grade` | 절대(사건 수준) | 절대(사건 수준) | 일치 | 1행 · 근거.md:68 · 11_viasat_2022-03-30.txt:46; 11_viasat_2022-03-30.txt:50 | 1행 · 근거.md:70 · 11_viasat_2022-03-30.txt:46, 50 · 01_eurepoc_1514.txt:4-5 | 절대(사건 수준) | 절대(사건 수준) (일치 · 그대로) |
| 20 | `effect_realized.value` | post | post | 일치 | 1행 · 근거.md:69 · 11_viasat_2022-03-30.txt:52 | 1행 · 근거.md:71 · 11_viasat_2022-03-30.txt:52 | post | post (일치 · 그대로) |
| 21 | `effect_realized.by_type` | {"1": "pre", "2": "pre", "3": "post"} | {"1": "pre", "2": "pre", "3": "post"} | 일치 | 3행 · 근거.md:70 · 11_viasat_2022-03-30.txt:40 | 3행 · 근거.md:72 · 11_viasat_2022-03-30.txt:40 | {"1": "pre", "2": "pre", "3": "post"} | {"1": "pre", "2": "pre", "3": "post"} (일치 · 그대로) |
| 22 | `effect_realized.boundary_flag` | false | false | 일치 | 1행 · 근거.md:73 · 11_viasat_2022-03-30.txt:46 | 1행 · 근거.md:75 · 11_viasat_2022-03-30.txt:46 | false | false (일치 · 그대로) |
| 23 | `effect_realized.note` (자유 서술) | ③ 파괴·교란은 식별 당일(2022-02-24) 발현 — 서비스 부분 중단·모뎀 무력화. ①·②는 피해 기업의 「최종 사용자 데이터 접근·침해 근거 없음」 서술에 따라 미발현(pre). 식별의 계기인 0302 UTC 악성 트래픽 탐… | ③ 파괴·교란 = post: 식별 시점(2022-02-24) 당일에 DoS 트래픽 탐지와 함께 수만 대 모뎀이 망에서 이탈했고 재접속을 시도하지 않았다 — 「Ultimately, tens of thousands of modems t… | 서술 차이 | 1행 · 근거.md:74 · 11_viasat_2022-03-30.txt:40 · 값 안 인용 줄 보완: 「최종 사용자 데이터 접근·침해 근거 없음」 줄 미상(미발견) | 1행 · 근거.md:76 · 11_viasat_2022-03-30.txt:40, 52, 54 · 「 」 없는 행 근거.md:76(표기 그대로): 위 by_type 행들의 구절 @ 11_viasat_2022-03-30.txt:40, 52, 54 | ③ 파괴·교란: 식별 시점(2022-02-24)에 서비스 거부로 「This targeted denial of service attack made it difficult for many modems to remain online.」(… | Fable r2 문구 그대로(부록 B) |
| 24 | `effect_realized.time_basis` (자유 서술) | 기준 시점 = 식별 시점 2022-02-24. 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic were detecte… | 기준 시점 = 식별 시점 2022-02-24. 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic were detecte… | 서술 차이 | 1행 · 근거.md:75 · 11_viasat_2022-03-30.txt:46; 11_viasat_2022-03-30.txt:36 | 1행 · 근거.md:77 · 11_viasat_2022-03-30.txt:46, 50 | 식별 시점 2022-02-24: 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic were detected」(11:46… | Fable r2 문구 그대로(부록 B) |
| 25 | `intrusion_state.value` | persisting | persisting | 일치 | 1행 · 근거.md:76 · 11_viasat_2022-03-30.txt:48; 11_viasat_2022-03-30.txt:50 | 1행 · 근거.md:78 · 11_viasat_2022-03-30.txt:48 | persisting | persisting (일치 · 그대로) |
| 26 | `intrusion_state.basis` (자유 서술) | 식별 시점(2022-02-24 0302 UTC 탐지) 뒤에도 공격이 수 시간 이어지고 관리 명령에 따른 모뎀 이탈이 0415 UTC 이후까지 계속됐다 — 식별 시점에 무단 접근 존속. 「As Viasat personnel engag… | 식별 시점(2022-02-24) 기준 — 식별 뒤에도 공격자의 트래픽 공격이 수 시간 이어졌고 관리 세그먼트에서의 파괴 명령 실행이 진행 중이었다 「As Viasat personnel engaged with Skylogic pers… | 서술 차이 | 1행 · 근거.md:77 · 11_viasat_2022-03-30.txt:38 | 1행 · 근거.md:79 · 11_viasat_2022-03-30.txt:50, 38 · 02_orkl_06ffedd8.txt:84-85 · 값 안 인용 줄 보완: 「ongoing attack」 → 02_orkl_06ffedd8.txt:84 (줄 보완 — 기계) | 식별 시점(2022-02-24 0302 UTC 탐지) 기준 무단 접근 존속: 「As Viasat personnel engaged with Skylogic personnel to triage the situation, and work… | Fable r2 문구 그대로(부록 B) |
| 27 | `countermeasure_availability` | (빈 값 "") | (빈 값 "") | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | (빈 값 "") | (빈 값) (그대로) |
| 28 | `conflict_nexus` | ambiguous | ambiguous | 일치 | 1행 · 근거.md:78 · 12_eu_hr_2022-05-10.txt:112 | 1행 · 근거.md:80 · 12_eu_hr_2022-05-10.txt:112 | ambiguous | ambiguous (일치 · 그대로) |
| 29 | `legal_characterization` | commitment_violation (12_eu_hr_2022-05-10.txt · 저자 검토 False) / use_of_force (12_eu_hr_2022-05-10.txt · 저자 검토 True) / commitment_v… | commitment_violation (12_eu_hr_2022-05-10.txt:114 · 저자 검토 True) / commitment_violation (13_us_state_2022-05-10.txt:59 · 저자 검토 Tru… | 값 불일치 — 항목 Opus 4 · Fable 2 | 4행 · 근거.md:82 · 12_eu_hr_2022-05-10.txt:114 | 2행 · 근거.md:84 · 12_eu_hr_2022-05-10.txt:114 | commitment_violation (12_eu_hr_2022-05-10.txt:114 · 저자 검토 True) / use_of_force (12_eu_hr_2022-05-10.txt:112 · 저자 검토 False) / use_… | 4항목 모두 채택(Opus r2 항목 구성): ① commitment_violation EU 12:114 / ② use_of_force EU 12:112 / ③ commitment_violation 미국 13:59 / ④ use_of_force 영국 15:58 |
| 30 | `responses` | monitoring · 미국 · 2022-03-17 · none_stated · 효과 post / criminal_investigation · 미국 · 2022-03-30 · none_stated · 효과 post / public_… | public_attribution · 유럽연합 · 2022-05-10 · UN 회원국이 설정한 책임 있는 국가 행동… · 효과 post / public_attribution · 미국 · 2022-05-10 · 규칙 기반 국제질서 —… | 값 불일치 — 항목 Opus 10 · Fable 8 | 10행 · 근거.md:86 · 01_eurepoc_1514.txt:3; 11_viasat_2022-03-30.txt:52 | 11행 · 근거.md:86 · 12_eu_hr_2022-05-10.txt:104, 110 | self_help_defense · 미국 · 2022-03-17 · none_stated · 효과 post / public_attribution · 유럽연합(이사회) · 2022-05-10 · none_stated · 효과 post… | 10항목: ⑴ self_help_defense·미국·2022-03-17 / ⑵ criminal_investigation·미국·2022-03-30 / ⑶ public_attribution·유럽연합·2022-05-10·invoked_legal_basis=Fable r2 문구(UN 회원국이 설정한 책임 있는 국가 행동 기대) / ⑷ public_attribution·미국·2022-05-10·invoked_legal_basis=Fable r2 문구(규칙 기반 국제질서) / ⑸ 영국 ⑹ 캐나다 ⑺ 호주 ⑻ 뉴질랜드 모두 public_attribution·2022-05-10·none_stated / ⑼ retorsion·subtype=sanction·뉴질랜드·2022-05-10 / ⑽ public_attribution·유럽연합·2022-07-19·none_stated. 모두 효과 post. (effect_at_response 근거 문구는 저자 미선택 — 조립 시 항목 출처 코더 판) |
| 31 | `aftermath` (자유 서술) | 2022-02-24 당일: 망 안정화·보안 완화 조치 즉시 개시, 수 시간 안에 대체로·수일 안에 완전히 안정화(11_viasat_2022-03-30.txt:38). 2022-03-15: EuRepoC 종료일·망 「stabilize… | 2022-02-24 식별 뒤 수 시간 내 망 대부분 안정화, 며칠 내 완전 안정화(11_viasat_2022-03-30.txt:38) · 2022-03-15 EuRepoC 기록상 망 「stabilized」(01_eurepoc_151… | 서술 차이 | 1행 · 근거.md:96 · 11_viasat_2022-03-30.txt:64; 01_eurepoc_1514.txt:5; 09_orkl_ba259eb4.… | 1행 · 근거.md:97 · 11_viasat_2022-03-30.txt:38, 64 · 01_eurepoc_1514.txt:3 · 04_orkl_a09… | 2022-02-24 이후 묶음 안의 후속(날짜순). 2022-02-24~: 망 안정화·복구 — 「the network was largely stabilized within hours and fully stabilized within… | Fable r2 문구 그대로(부록 B) |
| 32 | `tier` | v3_case | v3_case | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | v3_case | v3_case (일치 · 그대로) |
| 33 | `boundary_flag` | true | true | 일치 | 1행 · 근거.md:97 · 12_eu_hr_2022-05-10.txt:112 | 1행 · 근거.md:98 · — · 「 」 없는 행 근거.md:98(표기 그대로): conflict_nexus 요건 ⑶ 구절 없음(ambiguous 운용 규칙) — `conflict_nexu… @ — | true | true (일치 · 그대로) |
| 34 | `boundary_reason` (자유 서술) | conflict_nexus = ambiguous — 요건 ⑶(IHL 어휘의 원용이 관측) 구절 없음(묶음에 근거 없음). 요건 ⑴·⑵는 구절 있음(EU·미국 2022-05-10 성명). EU 성명의 「indiscriminate」는 … | conflict_nexus 3요건 가운데 ⑴ 무장분쟁의 존재·⑵ 작전과 분쟁의 관련성은 EU 선언(12_eu_hr_2022-05-10.txt:112, 114)과 미국 성명(13_us_state_2022-05-10.txt:57)에 구… | 서술 차이 | 1행 · 근거.md:98 · 12_eu_hr_2022-05-10.txt:112 · 값 안 인용 줄 보완: 「indiscriminate」 줄 미상(여러 곳 7) | 1행 · 근거.md:99 · 12_eu_hr_2022-05-10.txt:112, 114 · 13_us_state_2022-05-10.txt:57 · 「 」 없는 행 근거.md:99(표기 그대로): `conflict_nexus.req1`~`req3` 행의 구절 @ 12_eu_hr_2022-05-10.txt:112, 114 · 13_us_state_20… · 값 안 인용 줄 보완: 「indiscriminate communicatio…」 → 12_eu_hr_2022-05-10.txt:112 (줄 보완 — 기계) | ⑴ conflict_nexus 요건 ⑶(IHL 어휘 원용)이 EU 선언의 「indiscriminate」 한 낱말(12:112)에만 걸린다 — 통신 두절을 수식하는 서술적 용법이고 같은 문서는 행위를 「responsible State… | Fable r2 문구 그대로(부록 B) |
| 35 | `notes` (자유 서술) | ① 행위자 표기 갈림: EuRepoC 「initiator_name: Unknown」(01_eurepoc_1514.txt:16)이나 같은 기록의 사건명은 「Viasat Hack: Russian Military Intelligence … | ① 벤더·연구자·데이터셋의 법적·성격 규정(격하): EuRepoC 「il_breach_indicator: International telecommunication law;Due diligence;Sovereignty」(01_eure… | 서술 차이 | 1행 · 근거.md:99 · 01_eurepoc_1514.txt:16; 04_orkl_a097c1ac.txt:182; 01_eurepoc_1514.txt… · 값 안 인용 줄 보완: 「perpetrated」 → 22_orkl_572fe6bb.txt:364 (줄 보완 — 기계); 「GRU」 줄 미상(여러 곳 31) | 1행 · 근거.md:100 · 01_eurepoc_1514.txt:68, 77, 79 · 20_orkl_5ad57873.txt:64, 109 · 04_or… · 값 안 인용 줄 보완: 「initiator_name: Unknown」 → 01_eurepoc_1514.txt:16 (줄 보완 — 기계); 「Russia」 줄 미상(여러 곳 767); 「a really huge loss in commu…」 줄 미상(여러 곳 2); 「State Actors: Preventive me…」 → 01_eurepoc_1514.txt:38 (줄 보완 — 기계) | ① 벤더·데이터셋의 법적 규정(격하): EuRepoC il_breach_indicator 「International telecommunication law;Due diligence;Sovereignty」(01:68) · respon… | Fable r2 문구 그대로(부록 B) |
| 36 | `unit_type` | campaign | campaign | 일치 | 1행 · 근거.md:100 · 01_eurepoc_1514.txt:4; 01_eurepoc_1514.txt:5; 11_viasat_2022-03-30.tx… | 1행 · 근거.md:101 · 01_eurepoc_1514.txt:4-5 · 11_viasat_2022-03-30.txt:46-54 | campaign | campaign (일치 · 그대로) |
| 37 | `collection_mode` | organic | organic | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | organic | organic (일치 · 그대로) |
| 38 | `collection_mode_basis` (자유 서술) | 저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)으로 저자가 사례로 지정한 사건이다 — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니다. 회차 2 묶음에 더한 문서 7건은 저자 결정… | 저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)으로 저자가 사례로 지정한 사건이다 — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니다. 회차 2 묶음에 더한 문서 7건은 저자 결정… | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | 지시문 §1·manifest 「저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)」(manifest.json:3) — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니라 저자가 사례로 지정한… | 회차 2 템플릿 문구 그대로(묶음 보충 결정 문장 포함) |
| 39 | `target_specificity` | specific_victim | specific_victim | 일치 | 1행 · 근거.md:101 · 11_viasat_2022-03-30.txt:36; 11_viasat_2022-03-30.txt:54 | 1행 · 근거.md:102 · 11_viasat_2022-03-30.txt:36 · 14_uk_ncsc_2022-05-10.txt:35 | specific_victim | specific_victim (일치 · 그대로) |
| 40 | `target_specificity_basis` (자유 서술) | 특정 위성망(KA-SAT)의 특정 소비자용 분할 구간을 겨냥한 고의 침투. 「On 24 February 2022, a multifaceted and deliberate cyber-attack against Viasat’s KA-SA… | 특정 피해 조직(Viasat KA-SAT 망의 소비자용 파티션)을 겨냥한 침투·파괴 「a multifaceted and deliberate cyber-attack against Viasat’s KA-SAT network」(11_vi… | 서술 차이 | 1행 · 근거.md:102 · 11_viasat_2022-03-30.txt:36 | 1행 · 근거.md:103 · 11_viasat_2022-03-30.txt:36, 46 · 14_uk_ncsc_2022-05-10.txt:35 | 「This incident was localized to a single consumer-oriented partition of the KA-SAT network」(11:36) · 「execute legitimate, targete… | Fable r2 문구 그대로(부록 B) |
| 41 | `victim_sector_sub` | communications, energy | communications, energy | 일치 | 2행 · 근거.md:53 · 11_viasat_2022-03-30.txt:36 | 1행 · 근거.md:104 · 01_eurepoc_1514.txt:15 · 04_orkl_a097c1ac.txt:7-8 | communications | [communications, energy] (일치 · 그대로) |
| 42 | `victim_sector_sub_note` (자유 서술) | 첫 값 communications = 주 표적(KA-SAT 위성 브로드밴드망 소비자용 분할 구간 · 피해 기관 Viasat/Skylogic와 그 가입자): 「On 24 February 2022, a multifaceted and d… | 주 표적(첫 값) = communications: 피해 기관은 위성 광대역 통신망 운영사 Viasat(KA-SAT)이고 EuRepoC도 7개 피해국 모두 「receiver_category: Critical infrastructure… | 서술 차이 | 1행 · 근거.md:55 · 14_uk_ncsc_2022-05-10.txt:41; 11_viasat_2022-03-30.txt:36 | 1행 · 근거.md:105 · 14_uk_ncsc_2022-05-10.txt:41 · 값 안 인용 줄 보완: 「receiver_category: Critical…」 → 01_eurepoc_1514.txt:14 (줄 보완 — 기계) | EuRepoC 「receiver_category: Critical infrastructure」(01:14) · 「receiver_subcategory: Telecommunications」(01:15); Viasat 「KA-SAT’s… | Fable r2 문구 그대로(부록 B) |
| 43 | `victim_assets` | d3fend:Radio Modem, d3fend:VPN Server | d3fend:Radio Modem, d3fend:VPN Server | 서술 차이 — 값 구조 같음 · quote·source만 다름 | 2행 · 근거.md:103 · 02_orkl_06ffedd8.txt:5 | 2행 · 근거.md:106 · 02_orkl_06ffedd8.txt:4-5 · 11_viasat_2022-03-30.txt:46, 54 | d3fend:Radio Modem, d3fend:VPN Server | Fable r2 인용 그대로: Radio Modem 02_orkl_06ffedd8.txt:4-5 / VPN Server 11_viasat_2022-03-30.txt:54 |
| 44 | `identified_date` | 2022-02-24 | 2022-02-24 | 일치 | — (메타 키 · 행 불요) | — (메타 키 · 행 불요) | 2022-02-24 | 2022-02-24 (일치 · 그대로) |

## 2. 회차 1 확정값 대비 바뀐 키(ⓑ · 키 · 회차 1 확정값 · Opus r2 · Fable r2 · 두 코더 모두 / 한쪽만)

> 회차 1 확정 레코드와 각 코더를 같은 판정 함수로 견준다. 값 불일치 · 한쪽 결측 = 값 바뀜, 서술 차이 = 서술 바뀜. 회차 1 확정의 자유 서술은 병합문(바탕 판 + 「(Opus) 추가 구절」)이라 서술 칸은 대부분 서술 바뀜으로 나온다.

### 2-1. 값이 바뀐 키 — 11(두 코더 모두 8 · Opus만 1 · Fable만 2)

| 키 | 회차 1 확정값 | Opus r2 (회차 1 대비) | Fable r2 (회차 1 대비) | 구분 | r2 두 코더끼리 |
|---|---|---|---|---|---|
| `alias` | EuRepoC 1514, Viasat Hack, KA-SAT 공격, AcidRain, ukrop, Russian Military Intelligence | GRU, Main Directorate of the General Staff of the Armed Forces of the Russian Federation, Russian Military In… (값 불일치 — 공통 1 · 회차 1만 5 · Opus만 2) | EuRepoC incident 1514, Viasat hack, KA-SAT Network cyber attack, AcidRain, ukrop, GRU, Main Directorate of th… (값 불일치 — 공통 2 · 회차 1만 4 · Fable만 5) | 두 코더 모두 | 값 불일치 |
| `actor` | Russian Military Intelligence | GRU (값 불일치) | Russian Military Intelligence (일치) | Opus만 | 값 불일치 |
| `c_id.grade` | 1 | 1 (일치) | 2 (값 불일치) | Fable만 | 값 불일치 |
| `c_id.source` | 11_viasat_2022-03-30.txt; 01_eurepoc_1514.txt; 04_orkl_a097c1ac.txt; 14_uk_ncsc_2022-05-10.txt; 13_us_state_2… | 20_orkl_5ad57873.txt; 16_s1_acidrain_2022-03-31.txt; 22_orkl_572fe6bb.txt; 14_uk_ncsc_2022-05-10.txt (값 불일치 — 가리키는 파일 다름) | 04_orkl_a097c1ac.txt:29-32 (값 불일치 — 가리키는 파일 다름) | 두 코더 모두 | 값 불일치 |
| `c_st.source` | 11_viasat_2022-03-30.txt; 01_eurepoc_1514.txt; 12_eu_hr_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt; 13_us_stat… | 12_eu_hr_2022-05-10.txt; 13_us_state_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt; 20_orkl_5ad57873.txt (값 불일치 — 가리키는 파일 다름) | 12_eu_hr_2022-05-10.txt:110; 13_us_state_2022-05-10.txt:57; 14_uk_ncsc_2022-05-10.txt:39; 15_uk_fcdo_2022-05-… (값 불일치 — 가리키는 파일 다름) | 두 코더 모두 | 값 불일치 |
| `victim_sector` | ict | ict, critical_infrastructure (값 불일치 — 공통 1 · 회차 1만 0 · Opus만 1) | critical_infrastructure (값 불일치 — 공통 0 · 회차 1만 1 · Fable만 1) | 두 코더 모두 | 값 불일치 |
| `victim_state` | 우크라이나 | 우크라이나 (일치) | 우크라이나(주 피해국) · 독일 · 폴란드 · 헝가리 · 그리스 · 이탈리아 · 프랑스(파급 피해국) (값 불일치) | Fable만 | 값 불일치 |
| `techniques` | T1498.001, T1133, T1072, T1485, T1561.001, T1529 | T1190, T1133, T1072, T1498.001, T1083, T1485, T1561.001, T1495, T1529 (값 불일치 — 공통 6 · 회차 1만 0 · Opus만 3) | T1498, T1190, T1133, T1072, T1485, T1561.001, T1495, T1529, T1083 (값 불일치 — 공통 5 · 회차 1만 1 · Fable만 4) | 두 코더 모두 | 값 불일치 |
| `legal_characterization` | commitment_violation (12_eu_hr_2022-05-10.txt:114 · 저자 검토 True) / use_of_force (12_eu_hr_2022-05-10.txt:112 ·… | commitment_violation (12_eu_hr_2022-05-10.txt · 저자 검토 False) / use_of_force (12_eu_hr_2022-05-10.txt · 저자 검토 … (값 불일치 — 항목 회차 1 3 · Opus 4) | commitment_violation (12_eu_hr_2022-05-10.txt:114 · 저자 검토 True) / commitment_violation (13_us_state_2022-05-1… (값 불일치 — 항목 회차 1 3 · Fable 2) | 두 코더 모두 | 값 불일치 |
| `responses` | self_help_defense · 미국 · 2022-03-17 · none_stated · 효과 post / public_attribution · 유럽연합(이사회) · 2022-05-10 · n… | monitoring · 미국 · 2022-03-17 · none_stated · 효과 post / criminal_investigation · 미국 · 2022-03-30 · none_stated… (값 불일치 — 항목 회차 1 9 · Opus 10) | public_attribution · 유럽연합 · 2022-05-10 · UN 회원국이 설정한 책임 있는 국가 행동… · 효과 post / public_attribution · 미국 · 2022-… (값 불일치 — 항목 회차 1 9 · Fable 8) | 두 코더 모두 | 값 불일치 |
| `victim_sector_sub` | communications | communications, energy (값 불일치 — 공통 1 · 회차 1만 0 · Opus만 1) | communications, energy (값 불일치 — 공통 1 · 회차 1만 0 · Fable만 1) | 두 코더 모두 | 일치 |

### 2-2. 서술만 바뀐 키 — 14(두 코더 모두 14 · Opus만 0 · Fable만 0)

| 키 | 회차 1 확정값 | Opus r2 (회차 1 대비) | Fable r2 (회차 1 대비) | 구분 | r2 두 코더끼리 |
|---|---|---|---|---|---|
| `name` | Viasat KA-SAT 망 공격(2022) | Viasat KA-SAT 위성망 사이버 공격(2022) (서술 차이) | Viasat KA-SAT 위성 광대역망 공격(2022) (서술 차이) | 두 코더 모두 | 서술 차이 |
| `c_id.basis` | 식별 시점(2022-02-24) 기준: 묶음 안에 이 시점의 행위자 식별 서술이 없다 — Viasat 개요는 「high volumes of focused, malicious traffic were… | 식별 시점(2022-02-24) 등급 1 — 식별 시점에 이 작전을 특정 행위자 집단에 연결한 서술이 묶음에 없다. 「ViaSat quickly suspected that disruptions c… (서술 차이) | 식별 시점(2022-02-24) 기준 등급 2(추정 보도 수준). 식별 당일 묶음에는 행위자를 지목한 문서가 없고, 사후 서술이 당시의 추정만 전한다 — 「The timing coincided w… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `c_st.basis` | 식별 시점(2022-02-24) 기준 등급 1: 묶음 안에 이 시점의 국가 귀속 서술이 없다(Viasat 개요는 「an attacker」(11:54), EuRepoC initiator_name 「… | 귀속 기준일(2022-05-10 · 첫 공식 귀속 성명일) 등급 4 — 국가(러시아)를 수행 주체로 단정하나 국가기관(소속)은 특정하지 않는다(등급 5 「국가기관 소속 특정」 미충족). 「The … (서술 차이) | 귀속 기준일(2022-05-10 · 첫 공식 귀속 성명일) 기준 등급 4 — 국가(러시아 연방)의 행위라고 단정하되 국가기관(조직)은 특정하지 않음. EU 「strongly condemn the … (서술 차이) | 두 코더 모두 | 서술 차이 |
| `access_depth.basis` | 「Subsequent investigation and forensic analysis identified a ground-based network intrusion by an attacker ex… | 한 침투 안의 최댓값 = 운영자 망의 신뢰 관리 구간(특권 자산). 「Subsequent investigation and forensic analysis identified a ground-bas… (서술 차이) | 공격자가 VPN 장비의 설정 오류를 통해 KA-SAT 망의 신뢰된 관리 세그먼트에 원격 접근하고, 망을 관리·운영하는 특정 네트워크 세그먼트까지 횡적 이동한 뒤 그 접근으로 다수 모뎀에 관리 명령… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `effect_realized.note` | ③ 파괴·교란: 식별 시점(2022-02-24)에 서비스 거부로 「This targeted denial of service attack made it difficult for many modems… | ③ 파괴·교란은 식별 당일(2022-02-24) 발현 — 서비스 부분 중단·모뎀 무력화. ①·②는 피해 기업의 「최종 사용자 데이터 접근·침해 근거 없음」 서술에 따라 미발현(pre). 식별의 계… (서술 차이) | ③ 파괴·교란 = post: 식별 시점(2022-02-24) 당일에 DoS 트래픽 탐지와 함께 수만 대 모뎀이 망에서 이탈했고 재접속을 시도하지 않았다 — 「Ultimately, tens of t… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `effect_realized.time_basis` | 식별 시점 2022-02-24: 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic … | 기준 시점 = 식별 시점 2022-02-24. 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious … (서술 차이) | 기준 시점 = 식별 시점 2022-02-24. 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious … (서술 차이) | 두 코더 모두 | 서술 차이 |
| `intrusion_state.basis` | 식별 시점(2022-02-24 0302 UTC 탐지) 기준 무단 접근 존속: 「As Viasat personnel engaged with Skylogic personnel to triage the… | 식별 시점(2022-02-24 0302 UTC 탐지) 뒤에도 공격이 수 시간 이어지고 관리 명령에 따른 모뎀 이탈이 0415 UTC 이후까지 계속됐다 — 식별 시점에 무단 접근 존속. 「As Vi… (서술 차이) | 식별 시점(2022-02-24) 기준 — 식별 뒤에도 공격자의 트래픽 공격이 수 시간 이어졌고 관리 세그먼트에서의 파괴 명령 실행이 진행 중이었다 「As Viasat personnel engage… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `aftermath` | 2022-02-24 이후 묶음 안의 후속(날짜순). 2022-02-24~: 망 안정화·복구 — 「the network was largely stabilized within hours and ful… | 2022-02-24 당일: 망 안정화·보안 완화 조치 즉시 개시, 수 시간 안에 대체로·수일 안에 완전히 안정화(11_viasat_2022-03-30.txt:38). 2022-03-15: EuRe… (서술 차이) | 2022-02-24 식별 뒤 수 시간 내 망 대부분 안정화, 며칠 내 완전 안정화(11_viasat_2022-03-30.txt:38) · 2022-03-15 EuRepoC 기록상 망 「stabil… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `boundary_reason` | ⑴ conflict_nexus 요건 ⑶(IHL 어휘 원용)이 EU 선언의 「indiscriminate」 한 낱말(12:112)에만 걸린다 — 통신 두절을 수식하는 서술적 용법이고 같은 문서는 행위… | conflict_nexus = ambiguous — 요건 ⑶(IHL 어휘의 원용이 관측) 구절 없음(묶음에 근거 없음). 요건 ⑴·⑵는 구절 있음(EU·미국 2022-05-10 성명). EU 성명… (서술 차이) | conflict_nexus 3요건 가운데 ⑴ 무장분쟁의 존재·⑵ 작전과 분쟁의 관련성은 EU 선언(12_eu_hr_2022-05-10.txt:112, 114)과 미국 성명(13_us_state_2… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `notes` | ① 벤더·데이터셋의 법적 규정(격하): EuRepoC il_breach_indicator 「International telecommunication law;Due diligence;Sovereig… | ① 행위자 표기 갈림: EuRepoC 「initiator_name: Unknown」(01_eurepoc_1514.txt:16)이나 같은 기록의 사건명은 「Viasat Hack: Russian Mi… (서술 차이) | ① 벤더·연구자·데이터셋의 법적·성격 규정(격하): EuRepoC 「il_breach_indicator: International telecommunication law;Due diligence;… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `collection_mode_basis` | 지시문 §1·manifest 「저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)」(manifest.json:3) — 특정 라벨·시점 상태를 메우려는 표적… | 저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)으로 저자가 사례로 지정한 사건이다 — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니다. 회차 2 묶음… (서술 차이) | 저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)으로 저자가 사례로 지정한 사건이다 — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니다. 회차 2 묶음… (서술 차이) | 두 코더 모두 · 두 코더 값 = 회차 2 템플릿 값 | 일치 |
| `target_specificity_basis` | 「This incident was localized to a single consumer-oriented partition of the KA-SAT network」(11:36) · 「execute… | 특정 위성망(KA-SAT)의 특정 소비자용 분할 구간을 겨냥한 고의 침투. 「On 24 February 2022, a multifaceted and deliberate cyber-attack ag… (서술 차이) | 특정 피해 조직(Viasat KA-SAT 망의 소비자용 파티션)을 겨냥한 침투·파괴 「a multifaceted and deliberate cyber-attack against Viasat’s K… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `victim_sector_sub_note` | EuRepoC 「receiver_category: Critical infrastructure」(01:14) · 「receiver_subcategory: Telecommunications」(01:1… | 첫 값 communications = 주 표적(KA-SAT 위성 브로드밴드망 소비자용 분할 구간 · 피해 기관 Viasat/Skylogic와 그 가입자): 「On 24 February 2022, … (서술 차이) | 주 표적(첫 값) = communications: 피해 기관은 위성 광대역 통신망 운영사 Viasat(KA-SAT)이고 EuRepoC도 7개 피해국 모두 「receiver_category: Cri… (서술 차이) | 두 코더 모두 | 서술 차이 |
| `victim_assets` | d3fend:Radio Modem, d3fend:VPN Server | d3fend:Radio Modem, d3fend:VPN Server (서술 차이 — 값 구조 같음 · quote·source만 다름) | d3fend:Radio Modem, d3fend:VPN Server (서술 차이 — 값 구조 같음 · quote·source만 다름) | 두 코더 모두 | 서술 차이 |

### 2-3. 두 코더 모두 회차 1 확정값과 같은 키 — 19

- `case_id` · `state_attribution` · `c_st.grade` · `c_st.reference_date` · `terminal_objective` · `access_depth.draft` · `timing_grade` · `effect_realized.value` · `effect_realized.by_type` · `effect_realized.boundary_flag` · `intrusion_state.value` · `countermeasure_availability` · `conflict_nexus` · `tier` · `boundary_flag` · `unit_type` · `collection_mode` · `target_specificity` · `identified_date`

## 3. 집합 · 목록 키 상세

- `alias` — Opus 3: GRU, Main Directorate of the General Staff of the Armed Forces of the Russian Federation, Russian Military Intelligence / Fable 7: EuRepoC incident 1514, Viasat hack, KA-SAT Network cyber attack, AcidRain, ukrop, GRU, Main Directorate of the General Staff of the Armed Forces of the Russian Federation / 회차 1 확정 6: EuRepoC 1514, Viasat Hack, KA-SAT 공격, AcidRain, ukrop, Russian Military Intelligence
  - 세 판 공통 0
  - Opus만(ⓐ) 1: Russian Military Intelligence
  - Fable만(ⓐ) 5: EuRepoC incident 1514, Viasat hack, KA-SAT Network cyber attack, AcidRain, ukrop
  - Opus r2에 새로(회차 1에 없음) 2: GRU, Main Directorate of the General Staff of the Armed Forces of the Russian Federation
  - Opus r2에서 빠짐(회차 1에만) 5: EuRepoC 1514, Viasat Hack, KA-SAT 공격, AcidRain, ukrop
  - Fable r2에 새로(회차 1에 없음) 5: EuRepoC incident 1514, Viasat hack, KA-SAT Network cyber attack, GRU, Main Directorate of the General Staff of the Armed Forces of the Russian Federation
  - Fable r2에서 빠짐(회차 1에만) 4: EuRepoC 1514, Viasat Hack, KA-SAT 공격, Russian Military Intelligence
- `techniques` — Opus 9: T1190, T1133, T1072, T1498.001, T1083, T1485, T1561.001, T1495, T1529 / Fable 9: T1498, T1190, T1133, T1072, T1485, T1561.001, T1495, T1529, T1083 / 회차 1 확정 6: T1498.001, T1133, T1072, T1485, T1561.001, T1529
  - 세 판 공통 5: T1133, T1072, T1485, T1561.001, T1529
  - Opus만(ⓐ) 1: T1498.001
  - Fable만(ⓐ) 1: T1498
  - Opus r2에 새로(회차 1에 없음) 3: T1190, T1083, T1495
  - Fable r2에 새로(회차 1에 없음) 4: T1498, T1190, T1495, T1083
  - Fable r2에서 빠짐(회차 1에만) 1: T1498.001
- `victim_sector` — Opus 2: ict, critical_infrastructure / Fable 1: critical_infrastructure / 회차 1 확정 1: ict
  - 세 판 공통 0
  - Opus만(ⓐ) 1: ict
  - Opus r2에 새로(회차 1에 없음) 1: critical_infrastructure
  - Fable r2에 새로(회차 1에 없음) 1: critical_infrastructure
  - Fable r2에서 빠짐(회차 1에만) 1: ict
  - 첫 값(주 표적): Opus ict / Fable critical_infrastructure / 회차 1 ict
- `victim_sector_sub` — Opus 2: communications, energy / Fable 2: communications, energy / 회차 1 확정 1: communications
  - 세 판 공통 1: communications
  - Opus r2에 새로(회차 1에 없음) 1: energy
  - Fable r2에 새로(회차 1에 없음) 1: energy
  - 첫 값(주 표적): Opus communications / Fable communications / 회차 1 communications
- `victim_assets` — Opus 2: d3fend:Radio Modem, d3fend:VPN Server / Fable 2: d3fend:Radio Modem, d3fend:VPN Server / 회차 1 확정 2: d3fend:Radio Modem, d3fend:VPN Server
  - 세 판 공통 2: d3fend:Radio Modem, d3fend:VPN Server

### 3-1. `legal_characterization` 값 구조별 항목 수(value — 서술 칸은 부록 B)

| 값 구조 | Opus | Fable | 회차 1 확정 |
|---|---:|---:|---:|
| commitment_violation | 2 | 2 | 1 |
| use_of_force | 2 | 0 | 2 |

| value · source · 저자 검토 플래그(항목 순) | Opus | Fable | 회차 1 |
|---|---|---|---|
| 0 | commitment_violation · 12_eu_hr_2022-05-10.txt · False | commitment_violation · 12_eu_hr_2022-05-10.txt:114 · True | commitment_violation · 12_eu_hr_2022-05-10.txt:114 · True |
| 1 | use_of_force · 12_eu_hr_2022-05-10.txt · True | commitment_violation · 13_us_state_2022-05-10.txt:59 · True | use_of_force · 12_eu_hr_2022-05-10.txt:112 · False |
| 2 | commitment_violation · 13_us_state_2022-05-10.txt · True | — | use_of_force · 15_uk_fcdo_2022-05-10.txt:58 · False |
| 3 | use_of_force · 15_uk_fcdo_2022-05-10.txt · True | — | — |

### 3-2. `responses` 값 구조별 항목 수(type · subtype · actor_state · date · invoked_legal_basis · effect_at_response.value — 서술 칸은 부록 B)

| 값 구조 | Opus | Fable | 회차 1 확정 |
|---|---:|---:|---:|
| monitoring · ∅ · 미국 · 2022-03-17 · none_stated · post | 1 | 0 | 0 |
| criminal_investigation · ∅ · 미국 · 2022-03-30 · none_stated · post | 1 | 0 | 0 |
| public_attribution · ∅ · 유럽연합 · 2022-05-10 · none_stated · post | 1 | 0 | 0 |
| public_attribution · ∅ · 미국 · 2022-05-10 · none_stated · post | 1 | 0 | 1 |
| public_attribution · ∅ · 영국 · 2022-05-10 · none_stated · post | 1 | 1 | 1 |
| public_attribution · ∅ · 캐나다 · 2022-05-10 · none_stated · post | 1 | 1 | 1 |
| public_attribution · ∅ · 호주 · 2022-05-10 · none_stated · post | 1 | 1 | 1 |
| public_attribution · ∅ · 뉴질랜드 · 2022-05-10 · none_stated · post | 1 | 1 | 1 |
| retorsion · sanction · 뉴질랜드 · 2022-05-10 · none_stated · post | 1 | 1 | 0 |
| public_attribution · ∅ · 유럽연합 · 2022-07-19 · none_stated · post | 1 | 1 | 0 |
| public_attribution · ∅ · 유럽연합 · 2022-05-10 · UN 회원국이 설정한 책임 있는 국가 행동 기대 — 「Such behaviour is contrary to… · post | 0 | 1 | 0 |
| public_attribution · ∅ · 미국 · 2022-05-10 · 규칙 기반 국제질서 — 「As nations committed to upholding the rules-b… · post | 0 | 1 | 0 |
| self_help_defense · ∅ · 미국 · 2022-03-17 · none_stated · post | 0 | 0 | 1 |
| public_attribution · ∅ · 유럽연합(이사회) · 2022-05-10 · none_stated · post | 0 | 0 | 1 |
| retorsion · ∅ · 뉴질랜드 · 2022-05-10 · none_stated · post | 0 | 0 | 1 |
| public_attribution · ∅ · 유럽연합(이사회) · 2022-07-19 · none_stated · post | 0 | 0 | 1 |

## 4. 근거 파일 보조 대조 — 항목 밖 행(저자 확정 참고)

### 4-1. `c_st` 두 시점(지시문 §3 · 양식 §A 개정 ⑵)

| 항목 | Opus r2 | Fable r2 | 두 코더 같음 | 회차 1 확정 |
|---|---|---|---|---|
| `c_st.reference_date` | 2022-05-10 | 2022-05-10 | 예 | 2022-05-10 |
| `c_st.grade`(기준일 등급) | 4 | 4 | 예 | 4 |
| 식별 시점 등급 — `c_st.basis`의 「식별 시점(2022-02-24) 기준 등급 N」 | 1 | 2 | 아니오 | 1 |
| 식별 시점 등급 — 근거 md `c_st.grade_2022-02-24` 행 | 1 — 근거.md:48 · 20_orkl_5ad57873.txt:98-99 | 2 — 근거.md:63 · 04_orkl_a097c1ac.txt:29-32 | 아니오 | — |
| 코더 안에서 basis 문구와 행의 수가 같은가 | 예 | 예 | | |

### 4-2. `conflict_nexus` 요건별 판정(근거 md §1 · 지시문 §3-2)

| 요건 | Opus r2 | Fable r2 | 같음 |
|---|---|---|---|
| ⑴ 무장분쟁의 존재 (`conflict_nexus.req1`) | 구절 있음 — 근거.md:79 · 12_eu_hr_2022-05-10.txt:112; 13_us_state_2022-05-10.txt:55 | 구절 있음 — ⑴ 무장분쟁의 존재 — 근거.md:81 · 12_eu_hr_2022-05-10.txt:112, 120 · 14_uk_ncsc_2022-05-10.tx… | 예 |
| ⑵ 그 작전과 분쟁의 관련성 (`conflict_nexus.req2`) | 구절 있음 — 근거.md:80 · 12_eu_hr_2022-05-10.txt:112; 13_us_state_2022-05-10.txt:57 | 구절 있음 — ⑵ 작전과 분쟁의 관련성(공… — 근거.md:82 · 12_eu_hr_2022-05-10.txt:112, 114 · 13_us_state_2022-05-10.t… | 예 |
| ⑶ IHL 어휘의 원용이 관측 (`conflict_nexus.req3`) | 구절 없음 — 근거.md:81 · — | 구절 없음 — ⑶ IHL 어휘의 원용이 관측 — 근거.md:83 · — | 예 |
| 판정값 `conflict_nexus` | ambiguous | ambiguous | 예 |

### 4-3. 근거 md §1에서 근거 구절 칸에 「 」이 없는 행(표기 그대로 · 「묶음에 근거 없음」 행 제외)

- Claude(Opus) 0행 — 없음
- Claude(Fable) 3행
  - 근거.md:76 `effect_realized.note` — 근거 구절 칸: 위 by_type 행들의 구절 · 파일:줄 칸: 11_viasat_2022-03-30.txt:40, 52, 54
  - 근거.md:98 `boundary_flag` — 근거 구절 칸: conflict_nexus 요건 ⑶ 구절 없음(ambiguous 운용 규칙) — `conflict_nexus.req3` 행 · 파일:줄 칸: —
  - 근거.md:99 `boundary_reason` — 근거 구절 칸: `conflict_nexus.req1`~`req3` 행의 구절 · 파일:줄 칸: 12_eu_hr_2022-05-10.txt:112, 114 · 13_us_state_2022-05-10.t…

### 4-4. `by_type` `pre` + 근거 칸 「묶음에 근거 없음」 꼴(건수만 · 치환하지 않음)

- Claude(Opus) 0
- Claude(Fable) 0

## 부록 A. 값 안 인용 줄 보완(④ · 두 코더 똑같이 · 원 산출은 고치지 않는다)

| 코더 | 값 경로 | 구절 | 결과 | 후보(여러 곳 · 앞 5) |
|---|---|---|---|---|
| Opus | `c_id.basis` | 「perpetrated」 | 22_orkl_572fe6bb.txt:364 (줄 보완 — 기계) | — |
| Opus | `c_st.basis` | 「국가기관 소속 특정」 | 줄 미상(미발견) | — |
| Opus | `effect_realized.note` | 「최종 사용자 데이터 접근·침해 근거 없음」 | 줄 미상(미발견) | — |
| Opus | `boundary_reason` | 「indiscriminate」 | 줄 미상(여러 곳 7) | 12_eu_hr_2022-05-10.txt:112, 20_orkl_5ad57873.txt:56, 22_orkl_572fe6bb.txt:842, 22_orkl_572fe6bb.txt:1232, 22_orkl_572fe6bb.txt:1333 … |
| Opus | `notes` | 「perpetrated」 | 22_orkl_572fe6bb.txt:364 (줄 보완 — 기계) | — |
| Opus | `notes` | 「GRU」 | 줄 미상(여러 곳 31) | 02_orkl_06ffedd8.txt:52, 04_orkl_a097c1ac.txt:131, 08_orkl_80592130.txt:21, 09_orkl_ba259eb4.txt:37, 09_orkl_ba259eb4.txt:363 … |
| Fable | `intrusion_state.basis` | 「ongoing attack」 | 02_orkl_06ffedd8.txt:84 (줄 보완 — 기계) | — |
| Fable | `boundary_reason` | 「indiscriminate communication outages」 | 12_eu_hr_2022-05-10.txt:112 (줄 보완 — 기계) | — |
| Fable | `notes` | 「initiator_name: Unknown」 | 01_eurepoc_1514.txt:16 (줄 보완 — 기계) | — |
| Fable | `notes` | 「Russia」 | 줄 미상(여러 곳 767) | 01_eurepoc_1514.txt:2, 01_eurepoc_1514.txt:3, 01_eurepoc_1514.txt:17, 01_eurepoc_1514.txt:33, 01_eurepoc_1514.txt:81 … |
| Fable | `notes` | 「a really huge loss in communications」 | 줄 미상(여러 곳 2) | 22_orkl_572fe6bb.txt:213-214, 22_orkl_572fe6bb.txt:395 |
| Fable | `notes` | 「State Actors: Preventive measures」 | 01_eurepoc_1514.txt:38 (줄 보완 — 기계) | — |
| Fable | `victim_sector_sub_note` | 「receiver_category: Critical infrastructure」 | 01_eurepoc_1514.txt:14 (줄 보완 — 기계) | — |

## 부록 B. 세 판(Opus r2 · Fable r2 · 회차 1 확정)이 모두 같지는 않은 필드의 전체 값

### `name`
- Opus r2:

```text
Viasat KA-SAT 위성망 사이버 공격(2022)
```
- Fable r2:

```text
Viasat KA-SAT 위성 광대역망 공격(2022)
```
- 회차 1 확정:

```text
Viasat KA-SAT 망 공격(2022)
```

### `alias`
- Opus r2:

```json
[
 "GRU",
 "Main Directorate of the General Staff of the Armed Forces of the Russian Federation",
 "Russian Military Intelligence"
]
```
- Fable r2:

```json
[
 "EuRepoC incident 1514",
 "Viasat hack",
 "KA-SAT Network cyber attack",
 "AcidRain",
 "ukrop",
 "GRU",
 "Main Directorate of the General Staff of the Armed Forces of the Russian Federation"
]
```
- 회차 1 확정:

```json
[
 "EuRepoC 1514",
 "Viasat Hack",
 "KA-SAT 공격",
 "AcidRain",
 "ukrop",
 "Russian Military Intelligence"
]
```

### `actor`
- Opus r2:

```text
GRU
```
- Fable r2:

```text
Russian Military Intelligence
```
- 회차 1 확정:

```text
Russian Military Intelligence
```

### `c_id.grade`
- Opus r2:

```json
1
```
- Fable r2:

```json
2
```
- 회차 1 확정:

```json
1
```

### `c_id.basis`
- Opus r2:

```text
식별 시점(2022-02-24) 등급 1 — 식별 시점에 이 작전을 특정 행위자 집단에 연결한 서술이 묶음에 없다. 「ViaSat quickly suspected that disruptions could be the result of a cyberattack. It directly affected satellite modems firmwares, but was still to be understood as of mid-March.」(20_orkl_5ad57873.txt:98-99) · 「No technical details became available; technical speculation has been rampant.」(16_s1_acidrain_2022-03-31.txt:42). 그 뒤의 상승(시점·서술어): 2022-03-24 익명 관리 인용 보도 제목 「Russian Military Behind Hack of Satellite Communication Devices in Ukraine at War’s Outset, U.S. Officials Say」(22_orkl_572fe6bb.txt:2521-2522) → 2022-05-10 정부 성명은 국가(러시아)만 지목하고 행위자 집단은 특정하지 않음 「The NCSC assesses that Russia was almost certainly responsible for the attack.」(14_uk_ncsc_2022-05-10.txt:39) → 2022-12-16 Carnegie 보고서가 단정 서술어 「perpetrated」로 GRU를 지목 「hackers working for the Main Directorate of the General Staff of the Armed Forces of the Russian Federation—commonly known as the GRU—perpetrated the so-called Viasat hack.」(22_orkl_572fe6bb.txt:363-364).
```
- Fable r2:

```text
식별 시점(2022-02-24) 기준 등급 2(추정 보도 수준). 식별 당일 묶음에는 행위자를 지목한 문서가 없고, 사후 서술이 당시의 추정만 전한다 — 「The timing coincided with the Russian invasion of Ukraine and suspicions arose that an attempt to take out Ukrainian military command-and-control capabilities by hindering satellite connectivity spilled over to affect German critical infrastructure. No technical details became available; technical speculation has been rampant.」(04_orkl_a097c1ac.txt:29-32). 이후 상승: 2022-03-31 SentinelLabs가 AcidRain과 VPNFilter 파괴 플러그인의 개발상 유사성을 중간 확신도로 평가 「We assess with medium-confidence that there are developmental similarities between AcidRain and a VPNFilter stage 3 destructive plugin.」(04_orkl_a097c1ac.txt:13-14) · 2022-05-10 영국 NCSC 「The NCSC assesses that Russia was almost certainly responsible for the attack.」(14_uk_ncsc_2022-05-10.txt:39) · 2022-12-16 Carnegie 「hackers working for the Main Directorate of the General Staff of the Armed Forces of the Russian Federation—commonly known as the GRU—perpetrated the so-called Viasat hack.」(22_orkl_572fe6bb.txt:363-364).
```
- 회차 1 확정:

```text
식별 시점(2022-02-24) 기준: 묶음 안에 이 시점의 행위자 식별 서술이 없다 — Viasat 개요는 「high volumes of focused, malicious traffic were detected」(11:46)와 「Subsequent investigation and forensic analysis identified a ground-based network intrusion by an attacker」(11:54)로 공격자를 「an attacker」로만 적고, EuRepoC는 initiator_name을 「Unknown」(01:16)으로 둔다. 이후 상승: 2022-03-31 SentinelLabs가 AcidRain과 VPNFilter의 「medium-confidence ... developmental similarities」(04:13-15)를 보고하되 「we cannot definitively tie AcidRain to VPNFilter (or the larger Sandworm threat cluster)」(04:182)라고 유보; 2022-05-10 영국 NCSC 「The NCSC assesses that Russia was almost certainly responsible for the attack」(14:39), 미국 「the United States is sharing publicly its assessment that Russia launched cyber attacks in late February against commercial satellite communications networks」(13:57), EU 「the malicious cyber activity conducted by the Russian Federation against Ukraine, which targeted the satellite KA-SAT network」(12:110). 행위자 집단명은 EuRepoC 사건명 「Russian Military Intelligence disrupted Ukrainian satellite broadband services」(01:2)에만 있고 정부 성명은 KA-SAT 공격에 대해 「Russia」·「Russian Federation」만 쓴다. (Opus) 추가 구절: 「That investigation is still ongoing.」(11_viasat_2022-03-30.txt:40) · 「While we cannot definitively tie AcidRain to VPNFilter (or the larger Sandworm threat cluster), we note a medium-confidence assessment of non-trivial developmental similarities between their components」(16_s1_acidrain_2022-03-31.txt:212) · 「The NCSC assesses that Russia was almost certainly responsible for the attack.」(14_uk_ncsc_2022-05-10.txt:39) · 「initiator_name: Unknown」(01_eurepoc_1514.txt:16)
```

### `c_id.source`
- Opus r2:

```text
20_orkl_5ad57873.txt; 16_s1_acidrain_2022-03-31.txt; 22_orkl_572fe6bb.txt; 14_uk_ncsc_2022-05-10.txt
```
- Fable r2:

```text
04_orkl_a097c1ac.txt:29-32
```
- 회차 1 확정:

```text
11_viasat_2022-03-30.txt; 01_eurepoc_1514.txt; 04_orkl_a097c1ac.txt; 14_uk_ncsc_2022-05-10.txt; 13_us_state_2022-05-10.txt; 12_eu_hr_2022-05-10.txt; 16_s1_acidrain_2022-03-31.txt
```

### `c_st.basis`
- Opus r2:

```text
귀속 기준일(2022-05-10 · 첫 공식 귀속 성명일) 등급 4 — 국가(러시아)를 수행 주체로 단정하나 국가기관(소속)은 특정하지 않는다(등급 5 「국가기관 소속 특정」 미충족). 「The European Union and its Member States, together with its international partners, strongly condemn the malicious cyber activity conducted by the Russian Federation against Ukraine, which targeted the satellite KA-SAT network, owned by Viasat.」(12_eu_hr_2022-05-10.txt:110) · 「the United States is sharing publicly its assessment that Russia launched cyber attacks in late February against commercial satellite communications networks to disrupt Ukrainian command and control during the invasion」(13_us_state_2022-05-10.txt:57) · 「The NCSC assesses that Russia was almost certainly responsible for the attack.」(14_uk_ncsc_2022-05-10.txt:39). 식별 시점(2022-02-24) 기준 등급 1 — 식별 시점의 국가 귀속 서술이 묶음에 없다(서술 부재). 「ViaSat quickly suspected that disruptions could be the result of a cyberattack. It directly affected satellite modems firmwares, but was still to be understood as of mid-March.」(20_orkl_5ad57873.txt:98-99). 사이 경과: 2022-03-24 익명 관리 인용 보도 「Russian Military Behind Hack of Satellite Communication Devices in Ukraine at War’s Outset, U.S. Officials Say」(22_orkl_572fe6bb.txt:2521-2522) — 공식 성명이 아니어서 기준일로 삼지 않음. 식별일에서 기준일까지 75일.
```
- Fable r2:

```text
귀속 기준일(2022-05-10 · 첫 공식 귀속 성명일) 기준 등급 4 — 국가(러시아 연방)의 행위라고 단정하되 국가기관(조직)은 특정하지 않음. EU 「strongly condemn the malicious cyber activity conducted by the Russian Federation against Ukraine, which targeted the satellite KA-SAT network, owned by Viasat.」(12_eu_hr_2022-05-10.txt:110) · 미국 「the United States is sharing publicly its assessment that Russia launched cyber attacks in late February against commercial satellite communications networks to disrupt Ukrainian command and control during the invasion」(13_us_state_2022-05-10.txt:57) · 영국 「The NCSC assesses that Russia was almost certainly responsible for the attack.」(14_uk_ncsc_2022-05-10.txt:39) · 「The NCSC also assesses that it is almost certain Russia was responsible for the subsequent cyber-attack impacting Viasat on 24 February.」(15_uk_fcdo_2022-05-10.txt:48). 식별 시점(2022-02-24) 기준 등급 2 — 식별 당일 공식 귀속 성명이 없고 침공과의 시간 일치에 따른 추정만 있었음 「The timing coincided with the Russian invasion of Ukraine and suspicions arose that an attempt to take out Ukrainian military command-and-control capabilities by hindering satellite connectivity spilled over to affect German critical infrastructure.」(04_orkl_a097c1ac.txt:29-32). 국가기관 특정(등급 5 해당)은 공식 성명이 아닌 자료에만 있음 — EuRepoC 「name: Viasat Hack: Russian Military Intelligence disrupted Ukrainian satellite broadband services in February 2022」(01_eurepoc_1514.txt:2) · 「state_responsibility_actor: Direct (official members of state entities / agencies / units responsible)」(01_eurepoc_1514.txt:67) · Carnegie(22_orkl_572fe6bb.txt:363-364).
```
- 회차 1 확정:

```text
식별 시점(2022-02-24) 기준 등급 1: 묶음 안에 이 시점의 국가 귀속 서술이 없다(Viasat 개요는 「an attacker」(11:54), EuRepoC initiator_name 「Unknown」(01:16)). 2022-05-10 기준 등급 4 — EU 「The European Union and its Member States, together with its international partners, strongly condemn the malicious cyber activity conducted by the Russian Federation against Ukraine, which targeted the satellite KA-SAT network, owned by Viasat.」(12_eu_hr_2022-05-10.txt:110); 영국 「The NCSC assesses that Russia was almost certainly responsible for the attack.」(14_uk_ncsc_2022-05-10.txt:39); 미국 「the United States is sharing publicly its assessment that Russia launched cyber attacks in late February against commercial satellite communications networks to disrupt Ukrainian command and control during the invasion」(13_us_state_2022-05-10.txt:57). 세 정부 문서 모두 국가(러시아)를 수행 주체로 단정하되 KA-SAT 공격에 대해서는 특정 국가기관을 명시하지 않는다(NCSC는 같은 문서에서 WhisperGate에만 「Russian Military Intelligence」를 쓴다 · 14:43). 국가기관 특정은 EuRepoC 사건명 「Russian Military Intelligence」(01:2)와 state_responsibility_actor 「Direct (official members of state entities / agencies / units responsible)」(01:67)에만 있고 initiator_name은 「Unknown」(01:16)이다. (Opus) 추가 구절: 「That investigation is still ongoing.」(11_viasat_2022-03-30.txt:40) · 「The NCSC also assesses that it is almost certain Russia was responsible for the subsequent cyber-attack impacting Viasat on 24 February.」(15_uk_fcdo_2022-05-10.txt:48) · 「The NCSC also assesses that the Russian Military Intelligence was almost certainly involved in the 13 January defacements of Ukrainian government websites and the deployment of Whispergate destructive malware.」(14_uk_ncsc_2022-05-10.txt:43)
```

### `c_st.source`
- Opus r2:

```text
12_eu_hr_2022-05-10.txt; 13_us_state_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt; 20_orkl_5ad57873.txt
```
- Fable r2:

```text
12_eu_hr_2022-05-10.txt:110; 13_us_state_2022-05-10.txt:57; 14_uk_ncsc_2022-05-10.txt:39; 15_uk_fcdo_2022-05-10.txt:48
```
- 회차 1 확정:

```text
11_viasat_2022-03-30.txt; 01_eurepoc_1514.txt; 12_eu_hr_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt; 13_us_state_2022-05-10.txt; 15_uk_fcdo_2022-05-10.txt
```

### `victim_sector`
- Opus r2:

```json
[
 "ict",
 "critical_infrastructure"
]
```
- Fable r2:

```json
[
 "critical_infrastructure"
]
```
- 회차 1 확정:

```json
[
 "ict"
]
```

### `victim_state`
- Opus r2:

```text
우크라이나
```
- Fable r2:

```text
우크라이나(주 피해국) · 독일 · 폴란드 · 헝가리 · 그리스 · 이탈리아 · 프랑스(파급 피해국)
```
- 회차 1 확정:

```text
우크라이나
```

### `techniques`
- Opus r2:

```json
[
 "T1190",
 "T1133",
 "T1072",
 "T1498.001",
 "T1083",
 "T1485",
 "T1561.001",
 "T1495",
 "T1529"
]
```
- Fable r2:

```json
[
 "T1498",
 "T1190",
 "T1133",
 "T1072",
 "T1485",
 "T1561.001",
 "T1495",
 "T1529",
 "T1083"
]
```
- 회차 1 확정:

```json
[
 "T1498.001",
 "T1133",
 "T1072",
 "T1485",
 "T1561.001",
 "T1529"
]
```

### `access_depth.basis`
- Opus r2:

```text
한 침투 안의 최댓값 = 운영자 망의 신뢰 관리 구간(특권 자산). 「Subsequent investigation and forensic analysis identified a ground-based network intrusion by an attacker exploiting a misconfiguration in a VPN appliance to gain remote access to the trusted management segment of the KA-SAT network. The attacker moved laterally through this trusted management network to a specific network segment used to manage and operate the network, and then used this network access to execute legitimate, targeted management commands on a large number of residential modems simultaneously.」(11_viasat_2022-03-30.txt:54). 위성·지상 기반시설 침해 근거 없음 — 「nor is there any evidence that the KA-SAT satellite itself or its supporting satellite ground infrastructure itself were directly involved, impaired or compromised.」(11_viasat_2022-03-30.txt:40). 진입 벡터(VPN 장비)와 도달 자산(관리망 → 가입자 모뎀)을 구분했다. 파괴형 페이로드가 이식된 곳은 가입자 위성 모뎀이며 OT 제어기가 아니다.
```
- Fable r2:

```text
공격자가 VPN 장비의 설정 오류를 통해 KA-SAT 망의 신뢰된 관리 세그먼트에 원격 접근하고, 망을 관리·운영하는 특정 네트워크 세그먼트까지 횡적 이동한 뒤 그 접근으로 다수 모뎀에 관리 명령을 실행했다 — 망 운영·관리 세그먼트(특권 자산)에 도달했으므로 core. 「exploiting a misconfiguration in a VPN appliance to gain remote access to the trusted management segment of the KA-SAT network. The attacker moved laterally through this trusted management network to a specific network segment used to manage and operate the network, and then used this network access to execute legitimate, targeted management commands on a large number of residential modems simultaneously.」(11_viasat_2022-03-30.txt:54). OT 환경 도달은 서술되지 않음 — 위성·지상 인프라 자체는 침해되지 않았고 「nor is there any evidence that the KA-SAT satellite itself or its supporting satellite ground infrastructure itself were directly involved, impaired or compromised.」(11_viasat_2022-03-30.txt:40), 풍력 터빈은 원격 감시·제어 통신만 끊겼음 「the wind turbines themselves were not rendered inoperable but “remote monitoring and control of the wind turbines” became unavailable due to issues with satellite communications.」(04_orkl_a097c1ac.txt:28-29).
```
- 회차 1 확정:

```text
「Subsequent investigation and forensic analysis identified a ground-based network intrusion by an attacker exploiting a misconfiguration in a VPN appliance to gain remote access to the trusted management segment of the KA-SAT network. The attacker moved laterally through this trusted management network to a specific network segment used to manage and operate the network, and then used this network access to execute legitimate, targeted management commands on a large number of residential modems simultaneously.」(11_viasat_2022-03-30.txt:54) — 망 운용·관리 세그먼트(특권 자산)에 도달해 명령을 실행했으므로 core. OT/ICS는 아니다: 「nor is there any evidence that the KA-SAT satellite itself or its supporting satellite ground infrastructure itself were directly involved, impaired or compromised」(11:40), 풍력 터빈은 「the wind turbines themselves were not rendered inoperable」(04:28).
```

### `effect_realized.note`
- Opus r2:

```text
③ 파괴·교란은 식별 당일(2022-02-24) 발현 — 서비스 부분 중단·모뎀 무력화. ①·②는 피해 기업의 「최종 사용자 데이터 접근·침해 근거 없음」 서술에 따라 미발현(pre). 식별의 계기인 0302 UTC 악성 트래픽 탐지가 곧 교란의 시작이어서 식별 시점에 효과가 이미 나타나 있었다. 「There is no evidence that any end-user data was accessed or compromised」(11_viasat_2022-03-30.txt:40)
```
- Fable r2:

```text
③ 파괴·교란 = post: 식별 시점(2022-02-24) 당일에 DoS 트래픽 탐지와 함께 수만 대 모뎀이 망에서 이탈했고 재접속을 시도하지 않았다 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52). ① 절취 = pre, ② 조작·공개 = pre: 데이터 접근·유출·공개 관측 없음 「There is no evidence that any end-user data was accessed or compromised, nor customer personal equipment (PCs, mobile devices, etc.) was improperly accessed」(11_viasat_2022-03-30.txt:40) · 「We believe the purpose of the attack was to interrupt service.」(11_viasat_2022-03-30.txt:40). 플래시 메모리 덧쓰기는 ③(파괴)으로 분류했다.
```
- 회차 1 확정:

```text
③ 파괴·교란: 식별 시점(2022-02-24)에 서비스 거부로 「This targeted denial of service attack made it difficult for many modems to remain online.」(11:46), 이어 「these destructive commands overwrote key data in flash memory on the modems, rendering the modems unable to access the network」(11:54) — 발현. ① 절취: 「There is no evidence that any end-user data was accessed or compromised」(11:40) — 미발현. ② 조작·공개: 「no evidence of any compromise or tampering with Viasat modem software or firmware images」(11:56), 공개된 자료 서술 없음 — 미발현. 플래시 메모리 덮어쓰기는 EuRepoC도 「Data corruption (deletion/altering)」(01:59)·「Disk Wipe」(01:45)로 ③ 계열로 적는다. (Opus) 추가 구절: 「Specifically, these destructive commands overwrote key data in flash memory on the modems, rendering the modems unable to access the network, but not permanently unusable.」(11_viasat_2022-03-30.txt:54) · 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52) · 「Spillover from this attack rendered 5,800 Enercon wind turbines in Germany unable to communicate for remote monitoring or control.」(16_s1_acidrain_2022-03-31.txt:24)
```

### `effect_realized.time_basis`
- Opus r2:

```text
기준 시점 = 식별 시점 2022-02-24. 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic were detected」(11_viasat_2022-03-30.txt:46) · 「On 24 February 2022, a multifaceted and deliberate cyber-attack against Viasat’s KA-SAT network resulted in a partial interruption of KA-SAT’s consumer-oriented satellite broadband service.」(11_viasat_2022-03-30.txt:36)
```
- Fable r2:

```text
기준 시점 = 식별 시점 2022-02-24. 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic were detected emanating from several SurfBeam2 and SurfBeam 2+ modems」(11_viasat_2022-03-30.txt:46) · 「This gradual decline of connected modems continued until approximately 0415 UTC, when Viasat and Skylogic observed larger numbers of modems across much of Europe exiting the network over the course of about 45 minutes.」(11_viasat_2022-03-30.txt:50).
```
- 회차 1 확정:

```text
식별 시점 2022-02-24: 「At approximately 0302 UTC on 24 February 2022, high volumes of focused, malicious traffic were detected」(11:46) · 「This gradual decline of connected modems continued until approximately 0415 UTC, when Viasat and Skylogic observed larger numbers of modems across much of Europe exiting the network over the course of about 45 minutes.」(11:50)
```

### `intrusion_state.basis`
- Opus r2:

```text
식별 시점(2022-02-24 0302 UTC 탐지) 뒤에도 공격이 수 시간 이어지고 관리 명령에 따른 모뎀 이탈이 0415 UTC 이후까지 계속됐다 — 식별 시점에 무단 접근 존속. 「As Viasat personnel engaged with Skylogic personnel to triage the situation, and worked to force the malicious modems offline, other modems emerged on the network to continue the targeted traffic-based attack throughout the next several hours」(11_viasat_2022-03-30.txt:48) · 「This gradual decline of connected modems continued until approximately 0415 UTC, when Viasat and Skylogic observed larger numbers of modems across much of Europe exiting the network over the course of about 45 minutes.」(11_viasat_2022-03-30.txt:50). 이후 안정화는 aftermath — 「the network was largely stabilized within hours and fully stabilized within several days」(11_viasat_2022-03-30.txt:38)
```
- Fable r2:

```text
식별 시점(2022-02-24) 기준 — 식별 뒤에도 공격자의 트래픽 공격이 수 시간 이어졌고 관리 세그먼트에서의 파괴 명령 실행이 진행 중이었다 「As Viasat personnel engaged with Skylogic personnel to triage the situation, and worked to force the malicious modems offline, other modems emerged on the network to continue the targeted traffic-based attack throughout the next several hours」(11_viasat_2022-03-30.txt:48) · 「This gradual decline of connected modems continued until approximately 0415 UTC」(11_viasat_2022-03-30.txt:50). 이후 축출·안정화는 aftermath — 「the network was largely stabilized within hours and fully stabilized within several days.」(11_viasat_2022-03-30.txt:38). 2022-03-31 Viasat은 여전히 「ongoing attack」을 언급 「Due to the ongoing investigation and to ensure the security of our systems from ongoing attack, we cannot publicly share all forensic details of the event.」(02_orkl_06ffedd8.txt:84-85).
```
- 회차 1 확정:

```text
식별 시점(2022-02-24 0302 UTC 탐지) 기준 무단 접근 존속: 「As Viasat personnel engaged with Skylogic personnel to triage the situation, and worked to force the malicious modems offline, other modems emerged on the network to continue the targeted traffic-based attack throughout the next several hours」(11:48); 탐지 뒤 0415 UTC에 모뎀 대량 이탈이 이어짐(11:50); 공격자는 관리 세그먼트에 접근해 명령을 실행하는 중이었음(11:54). 2022-03-31 시점 Viasat 「to ensure the security of our systems from ongoing attack」(02:84-85). (Opus) 추가 구절: 「the network was largely stabilized within hours and fully stabilized within several days」(11_viasat_2022-03-30.txt:38)
```

### `legal_characterization`
- Opus r2:

```json
[
 {
  "value": "commitment_violation",
  "quote": "Such behaviour is contrary to the expectations set by all UN Member States, including the Russian Federation, of responsible State behaviour and the intentions of States in cyberspace.",
  "source": "12_eu_hr_2022-05-10.txt",
  "needs_author_review": false
 },
 {
  "value": "use_of_force",
  "quote": "The cyberattack took place one hour before Russia’s unprovoked and unjustified invasion of Ukraine on 24 February 2022 thus facilitating the military aggression.",
  "source": "12_eu_hr_2022-05-10.txt",
  "needs_author_review": true
 },
 {
  "value": "commitment_violation",
  "quote": "As nations committed to upholding the rules-based international order in cyberspace, the United States and its allies and partners are taking steps to defend against Russia’s irresponsible actions.",
  "source": "13_us_state_2022-05-10.txt",
  "needs_author_review": true
 },
 {
  "value": "use_of_force",
  "quote": "We will continue to call out Russia’s malign behaviour and unprovoked aggression across land, sea and cyberspace, and ensure it faces severe consequences.",
  "source": "15_uk_fcdo_2022-05-10.txt",
  "needs_author_review": true
 }
]
```
- Fable r2:

```json
[
 {
  "value": "commitment_violation",
  "quote": "Such behaviour is contrary to the expectations set by all UN Member States, including the Russian Federation, of responsible State behaviour and the intentions of States in cyberspace.",
  "source": "12_eu_hr_2022-05-10.txt:114",
  "needs_author_review": true
 },
 {
  "value": "commitment_violation",
  "quote": "As nations committed to upholding the rules-based international order in cyberspace, the United States and its allies and partners are taking steps to defend against Russia’s irresponsible actions.",
  "source": "13_us_state_2022-05-10.txt:59",
  "needs_author_review": true
 }
]
```
- 회차 1 확정:

```json
[
 {
  "value": "commitment_violation",
  "quote": "This unacceptable cyberattack is yet another example of Russia’s continued pattern of irresponsible behaviour in cyberspace, which also formed an integral part of its illegal and unjustified invasion of Ukraine. Such behaviour is contrary to the expectations set by all UN Member States, including the Russian Federation, of responsible State behaviour and the intentions of States in cyberspace.",
  "source": "12_eu_hr_2022-05-10.txt:114",
  "needs_author_review": true
 },
 {
  "value": "use_of_force",
  "quote": "The cyberattack took place one hour before Russia’s unprovoked and unjustified invasion of Ukraine on 24 February 2022 thus facilitating the military aggression.",
  "source": "12_eu_hr_2022-05-10.txt:112",
  "needs_author_review": false
 },
 {
  "value": "use_of_force",
  "quote": "We will continue to call out Russia’s malign behaviour and unprovoked aggression across land, sea and cyberspace, and ensure it faces severe consequences.",
  "source": "15_uk_fcdo_2022-05-10.txt:58",
  "needs_author_review": false
 }
]
```

### `responses`
- Opus r2:

```json
[
 {
  "type": "monitoring",
  "actor_state": "미국",
  "date": "2022-03-17",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-03-17) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "criminal_investigation",
  "actor_state": "미국",
  "date": "2022-03-30",
  "invoked_legal_basis": "none_stated",
  "source": "11_viasat_2022-03-30.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-03-30) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "유럽연합",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "12_eu_hr_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "13_us_state_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "영국",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "15_uk_fcdo_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "캐나다",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "호주",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "뉴질랜드",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "retorsion",
  "actor_state": "뉴질랜드",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "subtype": "sanction",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-05-10) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "유럽연합",
  "date": "2022-07-19",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응일(2022-07-19) 이전인 2022-02-24에 교란 효과 발현 — 「Ultimately, tens of thousands of modems that were previously online and active dropped off the network, and these modems were not observed attempting to re-enter the network.」(11_viasat_2022-03-30.txt:52)"
  }
 }
]
```
- Fable r2:

```json
[
 {
  "type": "public_attribution",
  "actor_state": "유럽연합",
  "date": "2022-05-10",
  "invoked_legal_basis": "UN 회원국이 설정한 책임 있는 국가 행동 기대 — 「Such behaviour is contrary to the expectations set by all UN Member States, including the Russian Federation, of responsible State behaviour and the intentions of States in cyberspace.」(12_eu_hr_2022-05-10.txt:114)",
  "source": "12_eu_hr_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2022-05-10",
  "invoked_legal_basis": "규칙 기반 국제질서 — 「As nations committed to upholding the rules-based international order in cyberspace」(13_us_state_2022-05-10.txt:59)",
  "source": "13_us_state_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "영국",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "14_uk_ncsc_2022-05-10.txt; 15_uk_fcdo_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "뉴질랜드",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "retorsion",
  "subtype": "sanction",
  "actor_state": "뉴질랜드",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "캐나다",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "호주",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-05-10) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "유럽연합",
  "date": "2022-07-19",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "대응 개시 시점(2022-07-19) 이전인 2022-02-24에 모뎀 수만 대의 망 이탈·플래시 메모리 덧쓰기가 이미 발생 「tens of thousands of modems that were previously online and active dropped off the network」(11_viasat_2022-03-30.txt:52)"
  }
 }
]
```
- 회차 1 확정:

```json
[
 {
  "type": "self_help_defense",
  "actor_state": "미국",
  "date": "2022-03-17",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "2022-02-24에 모뎀 서비스 거부·플래시 덮어쓰기가 이미 발현(11:46·11:54); 「The US authorities (CISA and FBI) issued a warning on 17 March to US critical infrastructure companies of satellite communications (SATCOM) risks and \"possible threats.\"」(01:3)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "유럽연합(이사회)",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "12_eu_hr_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "「This cyberattack had a significant impact causing indiscriminate communication outages and disruptions across several public authorities, businesses and users in Ukraine, as well as affecting several EU Member States.」(12:112)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "미국",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "13_us_state_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "「The activity disabled very small aperture terminals in Ukraine and across Europe.」(13:57)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "영국",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "15_uk_fcdo_2022-05-10.txt; 14_uk_ncsc_2022-05-10.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "「incident on 24 February caused outages for several thousand Ukrainian customers, and impacted windfarms and internet users in central Europe」(15:42) · 「Viasat has said that “tens of thousands of terminals have been damaged, made inoperable and cannot be repaired.”」(15:52)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "뉴질랜드",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "EuRepoC political_response 「10.05.2022 ... State Actors: Stabilizing measures ... Statement by minister of foreign affairs (or spokesperson) ... New Zealand ... Nanaia Cybelle Mahuta (Foreign Minister, NZL)」(01:37-41); 효과는 2022-02-24에 발현(11:46·11:54)"
  }
 },
 {
  "type": "retorsion",
  "actor_state": "뉴질랜드",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "EuRepoC legal_response 「legal_response_date: 2022-5-10」 · 「legal_response_type: Peaceful means: Retorsion (International Law)」 · 「legal_response_subtype: Economic sanctions」 · 「legal_response_responding_country: New Zealand」(01:72-75); 효과는 2022-02-24에 발현(11:46·11:54)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "캐나다",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "EuRepoC political_response 「10.05.2022 ... State Actors: Stabilizing measures ... Statement by minister of foreign affairs (or spokesperson) ... Canada ... Government of Canada」(01:37-41); 효과는 2022-02-24에 발현(11:46·11:54)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "호주",
  "date": "2022-05-10",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "EuRepoC political_response 「10.05.2022 ... State Actors: Stabilizing measures ... Statement by minister of foreign affairs (or spokesperson) ... Australia ... Marise Payne (Minister for Foreign Affairs; Minister for Women, AUS)」(01:37-41); 효과는 2022-02-24에 발현(11:46·11:54)"
  }
 },
 {
  "type": "public_attribution",
  "actor_state": "유럽연합(이사회)",
  "date": "2022-07-19",
  "invoked_legal_basis": "none_stated",
  "source": "01_eurepoc_1514.txt",
  "effect_at_response": {
   "value": "post",
   "basis": "EuRepoC 「attribution_date: 19.07.2022 ... attributing_actor: High Representative of the Union for Foreign Affairs and Security Policy (HR/VP)」(01:23-26) · political_response 「19.07.2022 ... EU: Stabilizing measures ... Declaration of HR ... EU (region)」(01:37-41); 효과는 2022-02-24에 발현(11:46·11:54)"
  }
 }
]
```

### `aftermath`
- Opus r2:

```text
2022-02-24 당일: 망 안정화·보안 완화 조치 즉시 개시, 수 시간 안에 대체로·수일 안에 완전히 안정화(11_viasat_2022-03-30.txt:38). 2022-03-15: EuRepoC 종료일·망 「stabilized」(01_eurepoc_1514.txt:3·5). 같은 날 AcidRain 표본(ukrop)이 이탈리아에서 VirusTotal에 올라옴(04_orkl_a097c1ac.txt:71-72). 2022-03-17: 미 CISA·FBI가 자국 핵심기반시설에 위성통신(SATCOM) 위험 경고(01_eurepoc_1514.txt:3). 2022-03-24: 미 관리 인용 보도가 러시아군을 지목(22_orkl_572fe6bb.txt:2521-2522). 2022-03-30: Viasat 사고 개요 공개 — 교체 모뎀 약 3만 대 출하, 회사·고객이 여전히 영향을 받음(11_viasat_2022-03-30.txt:64 · 01_eurepoc_1514.txt:3). 2022-03-31: SentinelLabs AcidRain 분석 공개, Viasat가 그 분석이 자사 보고와 일치한다고 확인(16_s1_acidrain_2022-03-31.txt:36 · 02_orkl_06ffedd8.txt:39-43). 2022-05-10: EU·미국·영국·캐나다·호주·뉴질랜드 공개 귀속(12_eu_hr_2022-05-10.txt:110 · 13_us_state_2022-05-10.txt:57 · 15_uk_fcdo_2022-05-10.txt:48 · 01_eurepoc_1514.txt:37-41) — c_st 등급이 식별 시점 1에서 기준일 4로 상승(c_st.basis). 같은 날 뉴질랜드 경제 제재(01_eurepoc_1514.txt:72-76). 2022-07-19: EU 고위대표 선언(01_eurepoc_1514.txt:23·37-41). 2022-12-16: Carnegie 보고서가 GRU를 수행 주체로 서술(22_orkl_572fe6bb.txt:363-364). 2024-03-16: AcidRain 변종 AcidPour 발견, CERT-UA가 그 활동을 UAC-0165(Sandworm 하위 군집)에 귀속(09_orkl_ba259eb4.txt:39-47 · 09_orkl_ba259eb4.txt:355-357) — KA-SAT 공격 자체의 귀속은 아님.
```
- Fable r2:

```text
2022-02-24 식별 뒤 수 시간 내 망 대부분 안정화, 며칠 내 완전 안정화(11_viasat_2022-03-30.txt:38) · 2022-03-15 EuRepoC 기록상 망 「stabilized」(01_eurepoc_1514.txt:3) · 2022-03-15 AcidRain 표본(파일명 ukrop)이 이탈리아에서 VirusTotal에 업로드(04_orkl_a097c1ac.txt:71-72) · 2022-03-17 미국 CISA·FBI가 SATCOM 위험 경고 발령(01_eurepoc_1514.txt:3) · 2022-03-30 Viasat 사건 개요 공개(11_viasat_2022-03-30.txt:26) · 2022-03-31 SentinelLabs가 AcidRain을 공개하고 Viasat이 그 사용을 확인(04_orkl_a097c1ac.txt:17-18) · 보안연구자가 피해 모뎀 플래시 덤프로 파괴 패턴 확인(03_orkl_9bb5eb63.txt:18-19) · Viasat이 교체 모뎀 약 3만 대 출하(11_viasat_2022-03-30.txt:64) · 2022-05-10 EU·미국·영국이 러시아를 공개 귀속, EuRepoC 기록상 뉴질랜드·캐나다·호주도 성명·뉴질랜드 제재(12·13·14·15 · 01_eurepoc_1514.txt:37-41, 72-76) · 2022-07-19 EU HR 선언(01_eurepoc_1514.txt:23, 37-41) · 2024-03-16 AcidRain 변종 AcidPour 발견, CERT-UA가 그 활동을 UAC-0165(Sandworm 하위 클러스터)에 귀속(09_orkl_ba259eb4.txt:39-47, 355-357 · 08_orkl_80592130.txt:19-22). 인과 주장은 하지 않음.
```
- 회차 1 확정:

```text
2022-02-24 이후 묶음 안의 후속(날짜순). 2022-02-24~: 망 안정화·복구 — 「the network was largely stabilized within hours and fully stabilized within several days」(11:38), EuRepoC는 「While the Viasat network was "stabilized" by 15 March」(01:3)·end_date 15.03.2022(01:5); Viasat가 「nearly 30,000 modems」를 유통사에 발송(11:64). 2022-03-15: AcidRain 표본이 「uploaded to VirusTotal from Italy with the name ‘ukrop’」(04:71-72). 2022-03-17: 미국 CISA·FBI가 SATCOM 위험 경보 발령(01:3). 2022-03-30: Viasat가 사건 개요 공개(11:26·34). 2022-03-31: SentinelLabs가 AcidRain을 공개하고 VPNFilter와의 「medium-confidence」 개발 유사성을 보고(04:13-15); Viasat가 「the destructive executable that was run on the modems using a legitimate management command」로 확인(02:41-43). 2022-05-10: EU·미국·영국(및 EuRepoC 기록상 뉴질랜드·캐나다·호주)이 러시아를 공개 귀속(12:110·13:57·14:39·15:48·01:37-41), 뉴질랜드 경제제재(01:72-75) — c_st는 식별 시점 1에서 이 시점 4로 상승. 2022-07-19: EU HR 선언(01:23·01:37). 2024-03-16~21: AcidRain 변종 AcidPour 발견(09:39-47·08:11-13), CERT-UA가 그 활동을 「UAC-0165, considered a subgroup of the outdated Sandworm APT」로 귀속(09:355-357·08:19-22) — AcidPour 활동에 대한 귀속이며 KA-SAT 공격 자체의 귀속 서술은 아님.
```

### `boundary_reason`
- Opus r2:

```text
conflict_nexus = ambiguous — 요건 ⑶(IHL 어휘의 원용이 관측) 구절 없음(묶음에 근거 없음). 요건 ⑴·⑵는 구절 있음(EU·미국 2022-05-10 성명). EU 성명의 「indiscriminate」는 일반어라 ⑶으로 세지 않음 — 「This cyberattack had a significant impact causing indiscriminate communication outages and disruptions across several public authorities, businesses and users in Ukraine, as well as affecting several EU Member States.」(12_eu_hr_2022-05-10.txt:112)
```
- Fable r2:

```text
conflict_nexus 3요건 가운데 ⑴ 무장분쟁의 존재·⑵ 작전과 분쟁의 관련성은 EU 선언(12_eu_hr_2022-05-10.txt:112, 114)과 미국 성명(13_us_state_2022-05-10.txt:57)에 구절이 있으나, ⑶ IHL 어휘의 원용은 묶음의 국가·국제기구 문서에 구절이 없다(EU 선언의 「indiscriminate communication outages」는 일반어 사용). 따라서 ambiguous · 평시 트랙 잔류.
```
- 회차 1 확정:

```text
⑴ conflict_nexus 요건 ⑶(IHL 어휘 원용)이 EU 선언의 「indiscriminate」 한 낱말(12:112)에만 걸린다 — 통신 두절을 수식하는 서술적 용법이고 같은 문서는 행위를 「responsible State behaviour」 기대(12:114)로 규정한다. ⑵ actor: 집단명 「Russian Military Intelligence」는 EuRepoC 사건명(01:2)에만 있고 EuRepoC 구조 필드는 「Unknown」(01:16), 정부 성명은 「Russia」·「Russian Federation」만 쓴다(12:110·13:57·14:39). ⑶ c_st 2022-05-10 등급: 정부 문서가 국가를 수행 주체로 단정하나 기관을 특정하지 않아 4로 두었다(5와 갈릴 수 있음). (Opus) 추가 구절: 「indiscriminate communication outages」(12_eu_hr_2022-05-10.txt:112)
```

### `notes`
- Opus r2:

```text
① 행위자 표기 갈림: EuRepoC 「initiator_name: Unknown」(01_eurepoc_1514.txt:16)이나 같은 기록의 사건명은 「Viasat Hack: Russian Military Intelligence disrupted Ukrainian satellite broadband services in February 2022」(01_eurepoc_1514.txt:2), Carnegie(22)는 「perpetrated」 단정으로 GRU를 지목 — actor는 22의 표기 「GRU」. 2022-05-10 정부 성명은 국가(러시아)만 지목. ② Sandworm·APT28·UAC-0165는 이 작전의 수행 집단으로 지목되지 않음 — 「While we cannot definitively tie AcidRain to VPNFilter (or the larger Sandworm threat cluster)」(04_orkl_a097c1ac.txt:182), UAC-0165 귀속은 2024 AcidPour 활동(09_orkl_ba259eb4.txt:355-357)에 대한 것. alias에 넣지 않음. ③ 학술 DB·보안업체의 법적 규정(국가·국제기구·법원 아님 → notes로): 「il_breach_indicator: International telecommunication law;Due diligence;Sovereignty」(01_eurepoc_1514.txt:68) · 「attribution_legal_reference: International peace」(01_eurepoc_1514.txt:77) · 「response_indicator: Countermeasures under international law justified (state-atttribution & breach of international law)」(01_eurepoc_1514.txt:79) · Kaspersky 「questioning the rules for dual-use infrastructure during armed conflicts」(20_orkl_5ad57873.txt:112). ④ 공급망 공격 여부 갈림: SentinelOne 가설 「The threat actor used the KA-SAT management mechanism in a supply-chain attack to push a wiper designed for modems and routers.」(04_orkl_a097c1ac.txt:58-59) vs Viasat 「we don’t view this as a supply chain attack or vulnerability」(02_orkl_06ffedd8.txt:80) — T1195 미기입. ⑤ 금전 동기 서술 없음.
```
- Fable r2:

```text
① 벤더·연구자·데이터셋의 법적·성격 규정(격하): EuRepoC 「il_breach_indicator: International telecommunication law;Due diligence;Sovereignty」(01_eurepoc_1514.txt:68) · 「attribution_legal_reference: International peace」(01_eurepoc_1514.txt:77) · 「response_indicator: Countermeasures under international law justified (state-atttribution & breach of international law)」(01_eurepoc_1514.txt:79) — 연구 데이터셋 코딩이라 legal_characterization에 넣지 않음. Kaspersky 「sabotage」(20_orkl_5ad57873.txt:109) · 「ICS/OT wipers (AcidRain, Industroyer2)」(20_orkl_5ad57873.txt:64) — access_depth는 Viasat 서술(관리 세그먼트 도달)대로 core로 두었다. ② 행위자 표기: actor는 EuRepoC 제목의 「Russian Military Intelligence」(01_eurepoc_1514.txt:2)를 그대로 썼다. EuRepoC 「initiator_name: Unknown」·「initiator_country: Russia」(01_eurepoc_1514.txt:16-17). 2022-05-10 공식 성명은 「Russia」·「the Russian Federation」만 지목. Sandworm·UAC-0165 귀속은 2024년 AcidPour 활동에 대한 CERT-UA 귀속(08_orkl_80592130.txt:19-22 · 09_orkl_ba259eb4.txt:355-357)이고, AcidRain–VPNFilter(Sandworm) 연결은 중간 확신도의 개발상 유사성에 그친다 「we cannot definitively tie AcidRain to VPNFilter (or the larger Sandworm threat cluster)」(04_orkl_a097c1ac.txt:182) — alias에 넣지 않았다. ③ 묶음끼리 어긋나는 곳: SentinelLabs의 「supply-chain attack」 가설(04_orkl_a097c1ac.txt:58-59) vs Viasat 「no evidence of any supply-chain interference」(11_viasat_2022-03-30.txt:56) · 「we don’t view this as a supply chain attack or vulnerability」(02_orkl_06ffedd8.txt:80) — T1195는 넣지 않았다. Trustwave의 「exploitation of vulnerabilities in public facing applications such as the VPN appliances」(18_orkl_2d804484.txt:64-65) vs Viasat 「misconfiguration in a VPN appliance」(11_viasat_2022-03-30.txt:54). 군 통신 영향: Zhora의 「a really huge loss in communications」 vs 대변인 「no information that [the hack] worsened communications within Ukraine’s military」(22_orkl_572fe6bb.txt:395-400). ④ EuRepoC의 attribution_date는 19.07.2022(01_eurepoc_1514.txt:23)이나 묶음의 첫 공식 귀속 성명은 2022-05-10(12~15)이라 reference_date는 2022-05-10으로 했다. ⑤ responses에 넣지 않은 것: 미국 「State Actors: Preventive measures」·「Capacity building in third countries」(01_eurepoc_1514.txt:38-40)와 13_us_state_2022-05-10.txt:59의 우크라이나 지원은 11종 허용값에 맞는 것이 없음 · CISA·FBI 2022-03-17 SATCOM 경고(01_eurepoc_1514.txt:3)도 허용값 불일치 · 뉴질랜드·캐나다·호주 성명의 type은 EuRepoC 「Statement by minister of foreign affairs」와 number_attributions 8(01_eurepoc_1514.txt:21, 39)에서 public_attribution으로 옮긴 것이라 저자 확인 필요. ⑥ 금전 동기 서술 없음.
```
- 회차 1 확정:

```text
① 벤더·데이터셋의 법적 규정(격하): EuRepoC il_breach_indicator 「International telecommunication law;Due diligence;Sovereignty」(01:68) · response_indicator 「Countermeasures under international law justified (state-atttribution & breach of international law)」(01:79) · attribution_legal_reference 「International peace」(01:77) — 데이터셋 코딩이므로 legal_characterization에 넣지 않음. ② 행위자 연결 미확인: SentinelLabs의 VPNFilter(APT28·Sandworm·GRU) 유사성은 「medium-confidence」·「cannot definitively tie」(04:13-15·04:182); 「Sandworm」·「UAC-0165」·「GRU」는 2024년 AcidPour 활동과 VPNFilter에 대한 귀속(08:20-22·09:355-357·04:129-131)이라 alias에 넣지 않음. 02:52의 「Russian GRU hackers (Fancy Bear or Sandworm)」도 VPNFilter 귀속. ③ 기법에서 제외: 「moved laterally」(11:54)는 방법 미서술이라 기법 ID 없음; 03의 TR069 「APP INSTALL」·명령 주입은 연구자가 「I am not implying that any of these techniques were actually abused」(03:87-89)라 한 추정; VPN 자격증명 탈취·취약점 악용은 「unknowns」(03:92 · 질문 본문 03:93-95); DoS 단계의 우크라이나 내 모뎀이 어떻게 장악됐는지는 묶음에 서술 없음; SentinelLabs의 「supply-chain attack」 가설(04:58-61)은 Viasat가 「we don’t view this as a supply chain attack」(02:80)으로 부인. ④ 묶음 간 어긋남: Viasat 「no evidence of any compromise or tampering with Viasat modem software or firmware images」(11:56·02:37-38) vs SentinelLabs 와이퍼 배포 가설(04:179-181) — 이후 Viasat가 「destructive executable that was run on the modems using a legitimate management command」로 확인(02:41-43·16:36); 15:52의 「cannot be repaired」 vs 11:56 「The modems can be fully restored via a factory reset」. ⑤ 피해국: EuRepoC receiver_country 「Poland;Hungary;Greece;Ukraine;Germany;Italy;France」(01:11) — 주 피해국 우크라이나, 나머지는 파급(04:7-8·13:57). ⑥ responses 밖: 미국의 「new mechanisms to help Ukraine identify cyber threats and recover」·위성전화 지원(13:59, EuRepoC 「Capacity building in third countries」 01:38-39)은 허용 type 11종에 맞는 값이 없어 넣지 않음; Viasat의 「law enforcement and U.S. and international government agencies」 수사 협조(11:40·11:66)는 수사 주체 국가가 특정되지 않아 넣지 않음. 국제기구 성명(EU)은 「The European Union and its Member States」(12:110)가 주체라 회원국 공동 대응으로 보아 넣었다(판정 이유는 근거 파일 §3). ⑦ 금전 동기 서술 없음. ⑧ 「primary target is believed to have been the Ukrainian military」(14:41·15:50)·「to disrupt Ukrainian command and control」(13:57)는 의도 서술이므로 terminal_objective(비움)·victim_sector에 쓰지 않음. (Opus) 추가 구절: 「Although the primary target is believed to have been the Ukrainian military, other customers were affected, including personal and commercial internet users.」(14_uk_ncsc_2022-05-10.txt:41) · 「to disrupt Ukrainian command and control during the invasion」(13_us_state_2022-05-10.txt:57) · 「This cyber-attack did not impact Viasat’s directly managed mobility or government users on the KA-SAT satellite.」(11_viasat_2022-03-30.txt:36) · 「Russian Military Intelligence」(01_eurepoc_1514.txt:2) · 「initiator_name: Unknown」(01_eurepoc_1514.txt:16) · 「The modems can be fully restored via a factory reset.」(11_viasat_2022-03-30.txt:56)
```

### `collection_mode_basis`
- Opus r2:

```text
저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)으로 저자가 사례로 지정한 사건이다 — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니다. 회차 2 묶음에 더한 문서 7건은 저자 결정(검색어 언급 합계 10회 이상 결정론 규칙)으로 정했다.
```
- Fable r2:

```text
저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)으로 저자가 사례로 지정한 사건이다 — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니다. 회차 2 묶음에 더한 문서 7건은 저자 결정(검색어 언급 합계 10회 이상 결정론 규칙)으로 정했다.
```
- 회차 1 확정:

```text
지시문 §1·manifest 「저자 결정(우크라이나 사례 = Viasat KA-SAT · EuRepoC 1514)」(manifest.json:3) — 특정 라벨·시점 상태를 메우려는 표적 수집이 아니라 저자가 사례로 지정한 사건.
```

### `target_specificity_basis`
- Opus r2:

```text
특정 위성망(KA-SAT)의 특정 소비자용 분할 구간을 겨냥한 고의 침투. 「On 24 February 2022, a multifaceted and deliberate cyber-attack against Viasat’s KA-SAT network resulted in a partial interruption of KA-SAT’s consumer-oriented satellite broadband service.」(11_viasat_2022-03-30.txt:36) · 「This incident was localized to a single consumer-oriented partition of the KA-SAT network」(11_viasat_2022-03-30.txt:36) · 「execute legitimate, targeted management commands on a large number of residential modems simultaneously」(11_viasat_2022-03-30.txt:54)
```
- Fable r2:

```text
특정 피해 조직(Viasat KA-SAT 망의 소비자용 파티션)을 겨냥한 침투·파괴 「a multifaceted and deliberate cyber-attack against Viasat’s KA-SAT network」(11_viasat_2022-03-30.txt:36) · 「This incident was localized to a single consumer-oriented partition of the KA-SAT network」(11_viasat_2022-03-30.txt:36) · 「an operation targeting commercial communications company Viasat in Ukraine」(14_uk_ncsc_2022-05-10.txt:35). 우크라이나 내 모뎀이 DoS 트래픽 발원지로 쓰였으나(11_viasat_2022-03-30.txt:46) 그 모뎀 자체가 피해 망의 일부이므로 compromised_infrastructure가 아니다.
```
- 회차 1 확정:

```text
「This incident was localized to a single consumer-oriented partition of the KA-SAT network」(11:36) · 「execute legitimate, targeted management commands on a large number of residential modems simultaneously」(11:54) · 「Although the primary target is believed to have been the Ukrainian military, other customers were affected」(14:41) — 특정 망·특정 파티션의 피해자를 겨냥한 침투. 배치 전 도구 포착(capability_only)이 아니고, 피해 모뎀은 공격 도구가 아니라 표적(compromised_infrastructure 아님). (Opus) 추가 구절: 「strongly condemn the malicious cyber activity conducted by the Russian Federation against Ukraine, which targeted the satellite KA-SAT network, owned by Viasat」(12_eu_hr_2022-05-10.txt:110)
```

### `victim_sector_sub`
- Opus r2:

```json
[
 "communications",
 "energy"
]
```
- Fable r2:

```json
[
 "communications",
 "energy"
]
```
- 회차 1 확정:

```json
[
 "communications"
]
```

### `victim_sector_sub_note`
- Opus r2:

```text
첫 값 communications = 주 표적(KA-SAT 위성 브로드밴드망 소비자용 분할 구간 · 피해 기관 Viasat/Skylogic와 그 가입자): 「On 24 February 2022, a multifaceted and deliberate cyber-attack against Viasat’s KA-SAT network resulted in a partial interruption of KA-SAT’s consumer-oriented satellite broadband service.」(11_viasat_2022-03-30.txt:36). 둘째 값 energy = 파급 피해(독일 풍력 터빈 원격 감시·제어 상실): 「Spillover from this attack rendered 5,800 Enercon wind turbines in Germany unable to communicate for remote monitoring or control.」(16_s1_acidrain_2022-03-31.txt:24). 넣지 않은 것: 우크라이나 군 — 「Although the primary target is believed to have been the Ukrainian military」(14_uk_ncsc_2022-05-10.txt:41)은 추정 서술이고 Viasat는 「This cyber-attack did not impact Viasat’s directly managed mobility or government users on the KA-SAT satellite.」(11_viasat_2022-03-30.txt:36). 상위값 사상표(sub_to_top)가 이 디렉터리에 없어 communications→ict · energy→critical_infrastructure는 상위값 낱말 뜻(정보통신·필수기반)으로 맞췄다 — 저자 확인 필요.
```
- Fable r2:

```text
주 표적(첫 값) = communications: 피해 기관은 위성 광대역 통신망 운영사 Viasat(KA-SAT)이고 EuRepoC도 7개 피해국 모두 「receiver_category: Critical infrastructure」·「receiver_subcategory: Telecommunications」로 코딩(01_eurepoc_1514.txt:14-15). 둘째 값 energy = 파급 피해: 독일 Enercon 풍력 터빈 5,800기의 원격 감시·제어 통신 상실 「Spillover from this attack rendered 5,800 Enercon wind turbines in Germany unable to communicate for remote monitoring or control.」(04_orkl_a097c1ac.txt:7-8). 영국은 「the primary target is believed to have been the Ukrainian military」(14_uk_ncsc_2022-05-10.txt:41)라 하지만 군은 Viasat 고객(이용자)으로서 영향을 받은 것이고 피해 기관(공격받은 자산의 운영자)은 통신사다 — 저자 확인 대상.
```
- 회차 1 확정:

```text
EuRepoC 「receiver_category: Critical infrastructure」(01:14) · 「receiver_subcategory: Telecommunications」(01:15); Viasat 「KA-SAT’s consumer-oriented satellite broadband service」(11:34). 단일 주 표적 배정: 파급 피해인 독일 풍력 터빈 원격감시 두절(04:7-8 「rendered 5,800 Enercon wind turbines in Germany unable to communicate for remote monitoring or control」 · 13:57)은 energy 계열이지만 주 표적이 아니어서 제외; 「primary target is believed to have been the Ukrainian military」(14:41)는 피해 부문이 아니라 추정 의도 서술이므로 government_defense로 적지 않음. (Opus) 추가 구절: 「New UK and US intelligence suggests Russia was behind an operation targeting commercial communications company Viasat in Ukraine.」(14_uk_ncsc_2022-05-10.txt:35)
```

### `victim_assets`
- Opus r2:

```json
[
 {
  "value": "Radio Modem",
  "kind": "d3fend",
  "quote": "the KA-SAT satellite broadband service to wipe SATCOM modems on February 24",
  "source": "02_orkl_06ffedd8.txt:5"
 },
 {
  "value": "VPN Server",
  "kind": "d3fend",
  "quote": "exploiting a misconfiguration in a VPN appliance to gain remote access to the trusted management segment of the KA-SAT network",
  "source": "11_viasat_2022-03-30.txt:54"
 }
]
```
- Fable r2:

```json
[
 {
  "value": "Radio Modem",
  "kind": "d3fend",
  "quote": "deployed in the cyberattack that targeted the KA-SAT satellite broadband service to wipe SATCOM modems on February 24",
  "source": "02_orkl_06ffedd8.txt:4-5"
 },
 {
  "value": "VPN Server",
  "kind": "d3fend",
  "quote": "a ground-based network intrusion by an attacker exploiting a misconfiguration in a VPN appliance to gain remote access to the trusted management segment of the KA-SAT network",
  "source": "11_viasat_2022-03-30.txt:54"
 }
]
```
- 회차 1 확정:

```json
[
 {
  "value": "Radio Modem",
  "kind": "d3fend",
  "quote": "A newly discovered data wiper malware that wipes routers and modems has been deployed in the cyberattack that targeted the KA-SAT satellite broadband service to wipe SATCOM modems on February 24, affecting thousands in Ukraine and tens of thousands more across Europe.",
  "source": "02_orkl_06ffedd8.txt:4-6"
 },
 {
  "value": "VPN Server",
  "kind": "d3fend",
  "quote": "Subsequent investigation and forensic analysis identified a ground-based network intrusion by an attacker exploiting a misconfiguration in a VPN appliance to gain remote access to the trusted management segment of the KA-SAT network.",
  "source": "11_viasat_2022-03-30.txt:54"
 }
]
```
