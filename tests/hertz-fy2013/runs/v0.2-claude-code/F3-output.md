# Earnings quality and accruals: Hertz Global Holdings, Inc., FY2009 to Q4 FY2013

## 1. Header

```
Step:        F3, Earnings quality and accruals
Company:     Hertz Global Holdings, Inc. (SEC CIK 1364479), NYSE: HTZ [P0, header table]
Framework:   US GAAP [P0, header table; context sheet, Basis]
Currency:    USD. P1 in USD millions; text files in each filing's own units (thousands in the FY2011
             and FY2012 10-Ks and 10-Qs Q1 2011 to Q1 2013; millions elsewhere) [P0, header table].
             Every text figure used below was checked against its statement header; all figures here are USD millions.
Fiscal year: ends 31 December [P0]
Periods:     years FY2009 to FY2013; quarters Q1 FY2011 to Q4 FY2013; as of 31 March 2014 [P0]
Context:     context-sheet.md attached and used
Basis:       P1 as originally reported. FY2013 is also shown against FY2012 as revised in the FY2013 10-K (P66),
             because P1 FY2013 is on the corrected basis and P1 FY2012 is not (context sheet, Read first item 1; E24).
Conventions (they change the scores):
 - TATA uses the cash-flow form: (income from continuing operations - cash from operations) / total assets at t.
 - "Income from continuing operations" is the P1 line; for FY2009 to FY2011 it includes the noncontrolling
   interest (context sheet, Read first item 7).
 - The balance sheet is unclassified [P0, Known limits]. Current-asset lines = cash + restricted cash +
   receivables + inventories + prepaid expenses and other assets. Current-liability lines = accounts payable
   + accrued liabilities + accrued taxes. Debt is one line [P1, EXTRA]; it is treated as financing (all of it in
   dFIN, none in dWC) and all of it enters LVGI. Current portion of long-term debt, short-term and long-term
   investments are blank [P1, BS_A].
 - "Cash" means the P1 line "Cash and equivalents"; restricted cash is a non-cash current asset.
 - PP&E, net and Dep follow the workbook mapping: property and equipment only, rental fleet ("revenue earning
   equipment") excluded [P0, How statements.xlsx is made]. Alternative A in each table puts the fleet and its
   depreciation into PP&E and Dep.
 - AQI: right-of-use assets are zero (pre-ASC 842; none on the balance sheet) [P1, BS_A]; DEPI adds no
   right-of-use depreciation; LVGI adds no lease liabilities (none recognised).
 - GMI has no cost-of-sales line [P0, Known limits]; the cost figure is direct operating + depreciation of
   revenue earning equipment and lease charges [P1, EXTRA]. Alternative B sets GMI to 1.
 - Sloan accruals use total depreciation and amortization from the cash flow statement [P1, CF_A].
 - US-basis cash from operations (IFRS step) is not applicable: US GAAP reporter.
```

## 2. Summary

Items run: all 17 checklist rows in scope (B1 to B7, C1 to C8, C17, C19); B2, B3, B4 (AQI, GMI, LVGI) and B5 ran on the substitute lines stated in the header, and 11 sub-items could not run [calc, see Could not run]. Ledger: 18 rows, P1 1, P2 3, P3 8, P4 6.

- P1, F3-C8-01: in FY2013 the depreciation note reports U.S. car depreciation-rate reductions of $44.2 million and says the reductions were "indicative of the residual values experienced in the U.S." for 2013, while the same note reports $48.2 million of net losses on U.S. vehicle disposals attributed to "declining residual values" [P74, p. 126].
- P2, F3-C5-01: fleet depreciation per dollar of average gross fleet fell for three consecutive years (0.1629 to 0.1447) while net fleet capex per dollar of fleet depreciation rose for three (0.515 to 1.241) [calc].
- P2, F3-C8-02: the stated car holding-period range lengthened from 4 to 26 months (FY2011) to 4 to 28 (FY2012) to 4 to 36 (FY2013) with no change-in-estimate disclosure found [P11, p. 94; P39, p. 81; P68, p. 91; calc, search].
- P2, F3-C2-01: restructuring charges are adjusted out in 16 of 16 quarters and acquisition related costs in 15 of 16 [calc], while the releases list them under "extraordinary, unusual or non-recurring items" and the adjusted pre-tax definition refers to "certain one-time charges" [P271 to P295; P62, p. 50].

The M-score is below −1.78 in every pair under every mapping tried; the F-score is above 1.0 on the workbook mapping, which counts the rental fleet as a soft asset, and below 1.0 with the fleet in PP&E [calc, Tables 2 and 3]. These are reading priorities, not conclusions.

## 3. About the screens

The M-score and F-score rank companies for reading time. On SEC enforcement releases issued from 1982 to 2016, an M-score above −1.78 produced about 130 false flags for every true one, and an F-score above 1.0 about 108 (Beneish and Vorst, The Accounting Review, 2022, Table 2). Both were estimated on US companies reporting under US GAAP. A score above the cutoff is a reason to read the accounts it points to, not evidence about this company.

The F-score's unconditional probability of 0.0037 is the published version's figure as quoted in later work; the working-paper version used 0.00345 [unverified: the papers are not in the pack]. Issuance is 1 in every year here (debt issued and stock issued are both positive) [P1, CF_A; calc], so the model's lower score for a company that raised no capital does not arise.

## 4. Computation tables

Periods run across the columns. Every value marked [calc] was produced by the code in section 9; inputs are P1 cells unless a row says otherwise.

### 4.1 Accruals and decomposition (B1, B2, B3)

Table 1a. Accruals and decomposition (USD millions; ratios as decimals of average total assets)

| Line | FY2010 | FY2011 | FY2012 | FY2013 | FY2013 (FY2012 as revised) | Mark |
|---|---|---|---|---|---|---|
| Average total assets | 16667.3 | 17502.8 | 20479.8 | 23937.2 | 23926.3 | [calc] |
| Cash-flow accruals (NI - CFO) / avg TA | -0.1344 | -0.1164 | -0.1208 | -0.1355 | -0.1356 | [calc] |
| Balance-sheet accruals (Sloan, proxy lines) / avg TA | -0.1452 | -0.0927 | -0.0915 | -0.1051 | -0.1054 | [calc] |
| Gap: balance-sheet numerator minus cash-flow numerator | -180.4 | 414.8 | 600.0 | 726.6 | 721.0 | [calc] |
| dWC / avg TA | -0.0247 | 0.0227 | 0.0223 | 0.0097 | 0.0106 | [calc] |
| dNCO / avg TA | -0.0001 | 0.0662 | 0.2122 | 0.0418 | 0.0424 | [calc] |
| dFIN / avg TA | -0.0565 | -0.0006 | -0.2017 | -0.0360 | -0.0360 | [calc] |
| RSST accruals (dWC + dNCO + dFIN) / avg TA | -0.0813 | 0.0883 | 0.0328 | 0.0156 | 0.0170 | [calc] |
| dWC, dNCO, dFIN (USD m) | -411.7; -1.0; -942.0 | 398.0; 1158.4; -10.7 | 457.4; 4345.3; -4131.5 | 233.2; 1001.6; -860.8 | 253.6; 1014.5; -860.8 | [calc] |
| Identity check: dWC+dNCO+dFIN minus (d equity - d cash) | 0.0 | -0.1 | 0.1 | -0.0 | 0.0 | [calc] |

Table 1b. Trailing-four-quarter cash-flow accruals (quarters as originally reported, P1)

| Line | Q4 FY2011 | Q1 FY2012 | Q2 FY2012 | Q3 FY2012 | Q4 FY2012 | Q1 FY2013 | Q2 FY2013 | Q3 FY2013 | Q4 FY2013 | Mark |
|---|---|---|---|---|---|---|---|---|---|---|
| TTM income from continuing operations | 195.8 | 268.4 | 301.2 | 331.6 | 243.1 | 317.4 | 345.9 | 317.7 | 346.2 | [calc] |
| TTM cash from operations | 2233.3 | 2559.7 | 2704.8 | 2714.7 | 2717.9 | 2969.5 | 3018.1 | 3439.6 | 3589.6 | [calc] |
| Average total assets (opening = 4 quarters earlier) | 17502.8 | 17553.8 | 18868.5 | 19314.5 | 20479.8 | 21178.2 | 22680.9 | 22555.4 | 23937.2 | [calc] |
| Cash-flow accruals | -0.1164 | -0.1305 | -0.1274 | -0.1234 | -0.1208 | -0.1252 | -0.1178 | -0.1384 | -0.1355 | [calc] |

Table 1c. Reconciliation: balance-sheet change against the operating cash-flow line (USD millions; positive = source of cash)

| Line | FY2010 BS / CF / diff | FY2011 BS / CF / diff | FY2012 BS / CF / diff | FY2013 BS / CF / diff | FY2013 vs FY2012 as revised: BS / CF / diff | Mark |
|---|---|---|---|---|---|---|
| Receivables | -31.3 / -7.5 / -23.8 | -259.8 / -79.9 / -179.9 | -270.2 / -157.7 / -112.5 | 374.0 / -34.7 / 408.7 | 367.1 / -34.7 / 401.8 | [calc; CF line P1, CF_A] |
| Inventories + prepaid and other | -46.7 / -61.9 / 15.2 | -65.6 / 0.5 / -66.1 | -70.0 / -30.8 / -39.2 | -233.7 / -28.0 / -205.7 | -214.5 / -28.0 / -186.5 | [calc; CF line P1, EXTRA] |
| Accounts payable | 286.3 / 118.0 / 168.3 | -47.5 / -1.1 / -46.4 | 101.6 / 49.9 / 51.7 | -31.2 / 23.2 / -54.4 | -35.3 / 23.2 / -58.5 | [calc; P1, CF_A] |
| Accrued liabilities | 45.3 / -53.4 / 98.7 | 58.4 / -144.0 / 202.4 | 52.0 / -22.6 / 74.6 | -75.8 / 25.2 / -101.0 | -58.4 / 25.2 / -83.6 | [calc; P1, CF_A] |
| Accrued taxes | 0.5 / 0.3 / 0.2 | 16.9 / 15.2 / 1.7 | -7.2 / 2.8 / -10.0 | 21.8 / 24.5 / -2.7 | not run | [calc; P1, EXTRA] |
| Change in restricted cash (investing in the CF statement) | -157.6 | 100.4 | 263.6 | 288.3 | n/a | [calc] |
| Change in fleet-sale receivables (non-cash supplemental line) | -33.7 | 116.5 | -3.4 | -260.0 | n/a | [calc; P1, EXTRA] |
| Change in fleet purchases held in payables (non-cash supplemental line) | 125.4 | -112.8 | 96.0 | 39.5 | n/a | [calc; P1, EXTRA] |
| Deferred taxes (non-current accrual; CF add-back) | -26.1 | 68.1 | 128.8 | 241.3 | 241.3 | [P1, EXTRA] |
| Acquisitions, net of cash | 47.6 | 227.1 | 1,904.6 | 254.0 | 254.0 | [P1, CF_A] |
| BS-CF accrual gap / average total assets | -0.0108 | 0.0237 | 0.0293 | 0.0304 | not run | [calc] |

Reading Table 1:

- Both accrual measures are negative in every year, because the rental fleet's depreciation (USD 1,789.9m to 2,445.0m a year) is a non-cash charge while fleet purchases sit in investing [P1, IS_A and CF_A; calc]. On the RSST decomposition, dNCO is the largest component in FY2011, FY2012 and FY2013 and is offset by dFIN, which is the pattern of debt-financed fleet and acquisition growth [calc; inf: P1, context sheet E2, E9].
- The balance-sheet (Sloan) measure sits above the cash-flow measure by USD 414.8m, 600.0m and 726.6m in FY2011 to FY2013 [calc]. Each of those years has an acquisition or de-consolidation on the context sheet (E2 Donlen, E9 Dollar Thrifty, E15 China de-consolidation, E16 franchise re-acquisitions) [context sheet, section 4], so a gap is expected.
- Line-level, the FY2013 receivables difference of USD 408.7m is USD 260.0m of lower fleet-sale receivables (an investing item) plus the USD 45.9m provision for doubtful accounts shown on its own cash-flow line, leaving USD 102.8m (USD 118.5m after the USD 15.7m rise in property-sale receivables) not traced to a line in the pack [calc; P1, EXTRA]. The FY2013 prepaid-and-other difference of USD 205.7m coincides with the China Auto Rental investment, whose convertible notes were carried at USD 151.0m at year end [P81, p. 145; inf: P66, P81]; the balance-sheet line that holds the investment is not named in the notes searched [not found: P70, P81 searched for "China Auto Rental" with "prepaid" or "other assets"].
- The supplemental fleet-sale receivable and fleet-payable amounts behave as period-end balances (the 10-Q year-to-date values rise and fall within the year) [inf: P1, EXTRA quarterly columns; P66, p. 81].
- FY2010 has a gap of USD -180.4m with no acquisition or disposal on the context sheet [calc; context sheet, section 6]; most of the payables difference (USD 168.3m) lines up with the USD 125.4m rise in fleet purchases held in payables [calc; inf: P1, EXTRA]. P1 FY2009 and FY2010 are pre-revision (E4).

### 4.2 Beneish M-score (B4)

Table 2. Beneish M-score (workbook mapping: PP&E, net and Dep exclude the rental fleet)

| Line | FY2010 / FY2009 | FY2011 / FY2010 | FY2012 / FY2011 | FY2013 / FY2012 | FY2013 / FY2012 as revised | Mark |
|---|---|---|---|---|---|---|
| DSRI index | 0.9612 | 1.0858 | 1.0737 | 0.6714 | 0.6742 | [calc] |
| DSRI contribution (+0.920 x index) | +0.8843 | +0.9990 | +0.9878 | +0.6177 | +0.6203 | [calc] |
| GMI index | 0.8190 | 0.8484 | 0.9559 | 0.9942 | 1.0001 | [calc] |
| GMI contribution (+0.528 x index) | +0.4324 | +0.4479 | +0.5047 | +0.5249 | +0.5280 | [calc] |
| AQI index | 0.9268 | 1.0863 | 1.0625 | 1.0085 | 1.0090 | [calc] |
| AQI contribution (+0.404 x index) | +0.3744 | +0.4389 | +0.4292 | +0.4074 | +0.4076 | [calc] |
| SGI index | 1.0649 | 1.0973 | 1.0871 | 1.1941 | 1.1936 | [calc] |
| SGI contribution (+0.892 x index) | +0.9499 | +0.9788 | +0.9697 | +1.0652 | +1.0647 | [calc] |
| DEPI index | 1.0138 | 1.0430 | 1.0447 | 0.8985 | 0.8985 | [calc] |
| DEPI contribution (+0.115 x index) | +0.1166 | +0.1199 | +0.1201 | +0.1033 | +0.1033 | [calc] |
| SGAI index | 0.9733 | 1.0221 | 1.1674 | 0.9051 | 0.8846 | [calc] |
| SGAI contribution (-0.172 x index) | -0.1674 | -0.1758 | -0.2008 | -0.1557 | -0.1522 | [calc] |
| LVGI index | 1.0200 | 0.9835 | 1.0000 | 0.9884 | 0.9868 | [calc] |
| LVGI contribution (-0.327 x index) | -0.3336 | -0.3216 | -0.3270 | -0.3232 | -0.3227 | [calc] |
| TATA index | -0.1292 | -0.1153 | -0.1063 | -0.1319 | -0.1319 | [calc] |
| TATA contribution (+4.679 x index) | -0.6045 | -0.5394 | -0.4973 | -0.6172 | -0.6172 | [calc] |
| Constant | -4.8400 | -4.8400 | -4.8400 | -4.8400 | -4.8400 | [formula] |
| M-score (workbook mapping) | -3.188 | -2.892 | -2.854 | -3.218 | -3.208 | [calc] |
| Above -1.78? | no | no | no | no | no | [calc] |
| Alt. A: fleet in PP&E and Dep: AQI; DEPI; M | 0.9097; 1.0335; -3.192 | 1.0163; 1.0928; -2.915 | 1.3807; 1.0929; -2.719 | 0.9297; 0.9359; -3.245 | 0.9313; 0.9296; -3.236 | [calc] |
| Alt. B: GMI set to 1 (workbook mapping otherwise): M | -3.092 | -2.812 | -2.830 | -3.214 | -3.208 | [calc] |
| Alt. C: receivables less fleet-sale receivables: DSRI; M (fleet in PP&E) | 1.0166; -3.142 | 1.0645; -2.934 | 1.1727; -2.628 | 0.7622; -3.162 | 0.7675; -3.150 | [calc] |
| Cost-line gross margin t-1; t | 0.1529; 0.1867 | 0.1867; 0.2201 | 0.2201; 0.2302 | 0.2302; 0.2316 | 0.2316; 0.2316 | [calc] |

Comparability labels for each pair [context sheet, sections 4 and 6]:
- FY2010 / FY2009: no acquisition, disposal or lease-standard adoption on the context sheet; both years are pre-revision in P1 (E4) and carry depreciation-rate changes (E22).
- FY2011 / FY2010: **non-comparable years** (E2 Donlen acquisition, E3 locations acquired).
- FY2012 / FY2011: **non-comparable years** (E6 Cinelease, E9 Dollar Thrifty acquisition, E10 Advantage divestiture).
- FY2013 / FY2012: **non-comparable years** (E9 full year of Dollar Thrifty, E10, E15 China de-consolidation, E16); the P1 pair also mixes bases (E24), which the last column removes for FY2012.

Reading Table 2: M is below −1.78 in every pair under every mapping tried (workbook mapping, fleet in PP&E, GMI set to 1, receivables net of fleet-sale receivables) [calc]. The largest contributions in each pair are SGI (+0.95 to +1.07) and DSRI (+0.62 to +1.00), which are close to their neutral values (index about 1) and are the largest because of their coefficients [calc]. GMI has risen for three consecutive pairs (0.8190, 0.8484, 0.9559, 0.9942) while staying below 1, meaning the cost-line margin still improved each year (0.1529 in FY2009 to 0.2316 in FY2013) but by less each year [calc]. The cost line includes fleet depreciation, which the E22 rate changes lowered by USD 130.1m in FY2012 [P45, p. 113; calc], and the E24 revision moved vendor incentives from SG&A into fleet cost for FY2011 and FY2012 [context sheet, E24], so GMI and SGAI for pairs touching FY2011 and FY2012 are on a basis the revised filings no longer use [inf: context sheet E24, P68].

### 4.3 Dechow F-score (B5)

Table 3. Dechow F-score (workbook mapping: PP&E, net excludes the rental fleet)

| Line | FY2011 | FY2012 | FY2013 | FY2013 (FY2012 as revised) | Mark |
|---|---|---|---|---|---|
| RSST value | 0.0883 | 0.0328 | 0.0156 | 0.0170 | [calc] |
| RSST contribution (+0.790 x value) | +0.0698 | +0.0259 | +0.0123 | +0.0134 | [calc] |
| dREC value | 0.0148 | 0.0132 | -0.0156 | -0.0153 | [calc] |
| dREC contribution (+2.518 x value) | +0.0374 | +0.0332 | -0.0393 | -0.0386 | [calc] |
| dINV value | -0.0002 | 0.0011 | -0.0006 | -0.0006 | [calc] |
| dINV contribution (+1.191 x value) | -0.0002 | +0.0013 | -0.0007 | -0.0007 | [calc] |
| SOFT value | 0.8764 | 0.9154 | 0.9212 | 0.9212 | [calc] |
| SOFT contribution (+1.979 x value) | +1.7345 | +1.8116 | +1.8231 | +1.8231 | [calc] |
| dCS value | 0.0674 | 0.0886 | 0.2737 | 0.2713 | [calc] |
| dCS contribution (+0.171 x value) | +0.0115 | +0.0151 | +0.0468 | +0.0464 | [calc] |
| dEARN value | 0.0130 | 0.0007 | 0.0026 | 0.0028 | [calc] |
| dEARN contribution (-0.932 x value) | -0.0121 | -0.0006 | -0.0024 | -0.0026 | [calc] |
| ISS value | 1.0000 | 1.0000 | 1.0000 | 1.0000 | [calc] |
| ISS contribution (+1.029 x value) | +1.0290 | +1.0290 | +1.0290 | +1.0290 | [calc] |
| Constant | -7.8930 | -7.8930 | -7.8930 | -7.8930 | [formula] |
| Logit | -5.0232 | -4.9775 | -5.0242 | -5.0230 | [calc] |
| Probability | 0.00654 | 0.00684 | 0.00653 | 0.00654 | [calc] |
| F-score (workbook mapping) | 1.768 | 1.850 | 1.766 | 1.768 | [calc] |
| Above 1.0 / 1.85 / 2.45? | yes / no / no | yes / no / no | yes / no / no | yes / no / no | [calc] |
| Alt. A: fleet in PP&E: SOFT; contribution; F | 0.3047; +0.6029; 0.573 | 0.3611; +0.7146; 0.620 | 0.3440; +0.6807; 0.566 | 0.3440; +0.6807; 0.567 | [calc] |

Reading Table 3: on the workbook mapping the F-score is 1.768, 1.850 (1.8497 before rounding, below 1.85) and 1.766, above the 1.0 cutoff in all three years [calc]. The two largest contributions are soft assets (+1.73 to +1.82) and issuance (+1.029) [calc]. Soft assets are 0.88 to 0.92 of total assets on this mapping because the rental fleet, 0.55 to 0.58 of total assets, is outside the P1 PP&E line; goodwill and intangibles are 0.17 to 0.23 [calc]. With the fleet in PP&E (Alternative A), the score is 0.573, 0.620 and 0.566, below 1.0 [calc]. All three years straddle context-sheet acquisitions (E2, E6, E9, E16) or de-consolidation (E15), so each F-score compares non-comparable year-ends [context sheet, section 4].

### 4.4 Localization (B6, B7)

Table 4. Cash sales and growth gaps (decimals)

| Line | FY2010 | FY2011 | FY2012 | FY2013 | FY2013 vs FY2012 as revised | Mark |
|---|---|---|---|---|---|---|
| Cash sales = revenue - change in receivables (USD m) | 7531.2 | 8038.6 | 8750.6 | 11145.9 | 11139.0 | [calc] |
| Change in cash sales | n/a (needs FY2008 receivables) | 0.0674 | 0.0886 | 0.2737 | 0.2713 | [calc] |
| Revenue growth | 0.0649 | 0.0973 | 0.0871 | 0.1941 | 0.1936 | [calc] |
| Receivables growth | 0.0236 | 0.1915 | 0.1672 | -0.1982 | -0.1953 | [calc] |
| Receivables growth minus revenue growth | -0.0413 | 0.0942 | 0.0801 | -0.3924 | n/a | [calc] |
| Receivables excluding fleet-sale receivables: growth | 0.0826 | 0.1681 | 0.2748 | -0.0898 | -0.0839 | [calc; P1, EXTRA; P66, p. 81] |
| Same, minus revenue growth | 0.0176 | 0.0708 | 0.1877 | -0.2839 | n/a | [calc] |

Localization of the screens:
- M-score: not above −1.78 in any pair, so no account is mapped from it [calc].
- F-score (workbook mapping only): above 1.0; largest contributions soft assets and issuance [calc]. Soft assets map to capitalized costs and intangibles (step 6, Table 6): here the soft-asset share is dominated by the rental fleet and by goodwill and intangibles from the E9 acquisition [calc; context sheet, E9]. Issuance maps to no account.
- Cash sales rose 27.4% in FY2013 against revenue growth of 19.4% [calc], but FY2013 is not a year of high accruals (cash-flow accruals -0.1355, RSST 0.0156) [calc], so the pattern that step 4 describes (rising cash sales in a year of high accruals) is not present. The receivables fall behind the FY2013 cash-sales jump includes USD 260.0m of lower fleet-sale receivables [calc; P1, EXTRA].
- FY2012 receivables excluding fleet-sale receivables grew 27.5% against revenue growth of 8.7%, a gap of 18.8 percentage points [calc]; FY2012 includes E9 (Dollar Thrifty receivables of USD 170m acquired with 43 days of revenue) [context sheet, E9]. This is F2's area (A1 to A8); it is not the latest period, so it is not a row here.

### 4.5 Adjusted measures (C1 to C4)

Regime: Regulation G and Item 10(e) of Regulation S-K [P0, header table]. The releases are furnished under Items 2.02 and 7.01 of Form 8-K [P0, Known limits]; the adjusted pre-tax income measure also appears in the filed 10-K as the segment measure [P77, p. 131].

Table 5a. Adjusted-measure gap by quarter (USD millions; shares of revenue as decimals)

| Line | Q1 FY2011 | Q2 FY2011 | Q3 FY2011 | Q4 FY2011 | Q1 FY2012 | Q2 FY2012 | Q3 FY2012 | Q4 FY2012 | Q1 FY2013 | Q2 FY2013 | Q3 FY2013 | Q4 FY2013 | Mark |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Revenue (P1) | 1780.0 | 2072.3 | 2432.3 | 2013.8 | 1960.9 | 2225.1 | 2516.2 | 2318.5 | 2436.5 | 2714.6 | 3069.4 | 2551.3 | [P1, IS_Q] |
| GAAP pre-tax income (release) | -158.9 | 94.6 | 295.7 | 92.8 | -36.8 | 158.7 | 368.9 | -40.3 | 72.2 | 211.9 | 328.3 | 62.3 | [release] |
| Adjusted pre-tax income (release) | -16.0 | 184.4 | 346.9 | 165.1 | 29.4 | 233.9 | 424.8 | 213.5 | 144.5 | 314.5 | 519.5 | 186.3 | [release] |
| Pre-tax gap / revenue | 0.0803 | 0.0433 | 0.0211 | 0.0359 | 0.0338 | 0.0338 | 0.0222 | 0.1095 | 0.0297 | 0.0378 | 0.0623 | 0.0486 | [calc] |
| GAAP net income attributable (release) | -132.6 | 55.0 | 206.7 | 47.1 | -56.3 | 92.9 | 242.9 | -36.4 | 18.0 | 121.4 | 214.7 | -0.6 | [release] |
| Adjusted net income (release) | -14.2 | 116.6 | 223.2 | 104.0 | 19.4 | 154.4 | 280.3 | 140.9 | 93.9 | 204.4 | 337.7 | 121.1 | [release] |
| Net income gap / revenue | 0.0665 | 0.0297 | 0.0068 | 0.0283 | 0.0386 | 0.0276 | 0.0149 | 0.0765 | 0.0312 | 0.0306 | 0.0401 | 0.0477 | [calc] |
| GAAP diluted EPS; adjusted diluted EPS | -0.32; -0.03 | 0.12; 0.26 | 0.47; 0.51 | 0.11; 0.24 | -0.13; 0.05 | 0.21; 0.35 | 0.55; 0.63 | -0.09; 0.33 | 0.04; 0.21 | 0.27; 0.45 | 0.47; 0.73 | -0.00; 0.26 | [release] |
| Corporate EBITDA (release) | 166.4 | 362.1 | 525.7 | 335.2 | 208.0 | 407.7 | 607.0 | 412.8 | 367.1 | 540.4 | 740.8 | 405.5 | [release] |
| (Corporate EBITDA - GAAP pre-tax) / revenue | 0.1828 | 0.1291 | 0.0946 | 0.1204 | 0.1248 | 0.1119 | 0.0946 | 0.1954 | 0.1210 | 0.1210 | 0.1344 | 0.1345 | [calc] |
| Stock-based compensation added back (Corporate EBITDA table) | 9.1 | 7.6 | 7.8 | 6.6 | 7.4 | 7.5 | 7.3 | 8.0 | 7.9 | 11.7 | 11.2 | 3.7 | [release] |
| SBC / GAAP pre-tax income | n/m | 0.0803 | 0.0264 | 0.0711 | n/m | 0.0473 | 0.0198 | n/m | 0.1094 | 0.0552 | 0.0341 | 0.0594 | [calc] |
| SBC / revenue | 0.0051 | 0.0037 | 0.0032 | 0.0033 | 0.0038 | 0.0034 | 0.0029 | 0.0035 | 0.0032 | 0.0043 | 0.0036 | 0.0015 | [calc] |

Q4 FY2013 GAAP figures are those of the Q4 release (pre-tax USD 62.3m), not P1's derived Q4 (USD 50.7m), which absorbs nine-month corrections [P295, p. 2; P1, IS_Q; context sheet, Read first item 2]. The Q4 FY2012 adjusted pre-tax income first released as USD 213.5m is reprinted as USD 210.7m in the Q4 FY2013 release, with GAAP pre-tax moving from USD -40.3m to -43.1m by the same USD 2.8m (E24) [P285, p. 2; P295, p. 2; calc]. GAAP operating income is not presented, so SBC is shown against GAAP pre-tax income and revenue [P1, IS_Q "Operating income" blank]. SBC is reported for size only.

Table 5b. Presence matrix for the pre-tax reconciliation ("INCOME MEASUREMENTS" table of each release; 1 = present, 0 = absent). 2010 columns are the prior-year columns of the 2011 releases [P271 to P295, p. 1 or 2; calc]

| Category (company label) | Q1-Q4 FY2010 | Q1-Q4 FY2011 | Q1-Q4 FY2012 | Q1-Q4 FY2013 | Of last 8 | Of 16 | Label | Mark |
|---|---|---|---|---|---|---|---|---|
| Purchase accounting | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 8 | 16 | recurring | [calc] |
| Non-cash debt charges; "Debt-related charges" from Q4 FY2013 | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 8 | 16 | recurring; label changed | [calc] |
| Restructuring and related charges | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 8 | 16 | recurring | [calc] |
| Acquisition related costs (Q4 FY2012: "and charges") | 0 1 1 1 | 1 1 1 1 | 1 1 1 1 | 1 1 1 1 | 8 | 15 | recurring | [calc] |
| Integration expenses | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | 1 1 1 1 | 4 | 4 | new Q1 FY2013 | [calc] |
| Management transition costs | 0 0 0 0 | 1 0 1 0 | 0 0 0 0 | 0 0 0 0 | 0 | 2 | new Q1 FY2011 | [calc] |
| Premiums paid on debt | 0 0 0 0 | 1 1 0 0 | 0 0 0 0 | 0 0 0 1 | 1 | 3 | new Q1 FY2011 | [calc] |
| Derivative (gains) losses | 1 1 1 1 | 0 0 1 1 | 0 0 1 1 | 0 0 1 1 | 4 | 10 | none | [calc] |
| Pension adjustment (a gain) | 0 0 0 0 | 0 1 0 0 | 0 0 0 0 | 0 0 0 0 | 0 | 1 | new Q2 FY2011 | [calc] |
| Relocation costs | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | 0 0 1 1 | 2 | 2 | new Q3 FY2013 | [calc] |
| Impairment charges and other | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | 0 0 1 0 | 1 | 1 | new Q3 FY2013 | [calc] |
| Other | 0 0 0 0 | 0 0 0 0 | 0 0 0 1 | 0 1 1 1 | 4 | 4 | new Q4 FY2012 | [calc] |

Size of the recurring categories (sums of the quarterly releases, USD m): restructuring and related 66.3 (FY2011), 49.1 (FY2012), 100.2 (FY2013); acquisition related costs 18.7, 163.6, 19.9; purchase accounting 87.7, 109.9, 133.6 [calc]. Restructuring roughly doubled in FY2013 (+104%) [calc]. The quarterly sum for FY2013 restructuring differs by USD 1.4m from the FY2013 release's full-year 98.8 [calc; P295, p. 5].

Table 5c. Prominence (C4). Position = order of first mention in the headline block (title and bullets, before the dateline) and in the dateline paragraph through the CEO quotation [calc]

| Quarter | File | GAAP in headline block | First measure in headline block | GAAP in opening paragraph | First measure in opening paragraph | First 60 words of the opening (as filed) |
|---|---|---|---|---|---|---|
| Q1 FY2011 | P271, p. 1 | yes | adjusted | yes | adjusted | "HERTZ REPORTS SIGNIFICANT YEAR-OVER-YEAR FIRST QUARTER IMPROVEMENT AND RAISES GUIDANCE FOR 2011 · 2011 guidance increased for all metrics; adjusted diluted EPS up from $0.81 to $0.90 at the high end of the guidance range. · Worldwide revenues for the quarter up 7.2%, year-over-year, including worldwide equipment rental revenues up 13.2%. · Adjusted pre-tax loss(1) of $16.0 million for the" |
| Q2 FY2011 | P273, p. 1 | yes | GAAP | yes | adjusted | "HERTZ REPORTS SIGNIFICANT YEAR-OVER-YEAR SECOND QUARTER IMPROVEMENT AND RAISES GUIDANCE FOR 2011 · Worldwide revenues for the quarter up 10.3%, year-over-year, including worldwide equipment rental revenues up 13.5%. · GAAP pre-tax income for the second quarter of $94.6 million, versus a loss of $6.2 million in the second quarter of 2010. · Adjusted pre-tax income(1) of $184.4 million for the" |
| Q3 FY2011 | P275, p. 1 | yes | GAAP | yes | adjusted | "HERTZ REPORTS RECORD QUARTERLY INCOME · Worldwide revenues for the quarter up 11.3%, year-over-year, including worldwide equipment rental revenues up 14.4%, and record quarterly worldwide car rental revenues of $2.1 billion. · GAAP and adjusted pre-tax and net income, as well as the adjusted pre-tax and net income margins, were the highest in the Company’s history. · GAAP pre-tax income" |
| Q4 FY2011 | P277, p. 1 | yes | adjusted | yes | adjusted | "HERTZ SETS FINANCIAL RECORDS FOR FOURTH QUARTER AND FULL YEAR 2011 · Worldwide revenues for the quarter up 9.7% year-over-year (“YOY”). · Fourth quarter worldwide car rental revenues of $1,695.2 million, on record transaction days; worldwide equipment rental revenues increased 11.1% YOY; U.S. HERC fourth quarter rental rate revenue increased 15.5% YOY. · Record fourth quarter adjusted pre-tax margin of" |
| Q1 FY2012 | P279, p. 1 | yes | adjusted | yes | adjusted | "HERTZ REPORTS SIGNIFICANT YEAR-OVER-YEAR FIRST QUARTER IMPROVEMENT · Company increases 2012 guidance to $1.38 Adjusted EPS and $1.66B Corporate EBITDA at the high end of the range. · Worldwide revenues for the quarter up 10.2% year-over-year (“YOY”). · First quarter record worldwide car rental revenues of $1,658.2 million, on record transaction days; worldwide equipment rental revenues increased 12.6% YOY, U.S." |
| Q2 FY2012 | P281, p. 1 | yes | adjusted | yes | adjusted | "HERTZ REPORTS SIGNIFICANT YEAR-OVER-YEAR SECOND QUARTER IMPROVEMENT Company establishes several second quarter earnings records · Worldwide revenues for the quarter up 7.4% year-over-year (“YOY”), a 10.3% increase excluding foreign exchange. · Second quarter record worldwide car rental revenues of $1,889.6 million, on record transaction days; worldwide equipment rental revenues increased 11%, the sixth consecutive quarter of double-digit YOY growth. ·" |
| Q3 FY2012 | P283, p. 1 | yes | adjusted | yes | adjusted | "HERTZ REPORTS STRONG THIRD QUARTER IMPROVEMENT Company establishes several earnings records · Worldwide revenues for the quarter up 3.4% year-over-year (“YOY”), a 6.4% increase excluding foreign exchange. · Record worldwide car rental revenues of $2,152.6 million in the third quarter, on record transaction days. · Worldwide equipment rental revenues increased 12.8%, the seventh consecutive quarter of double-digit YOY growth, driven" |
| Q4 FY2012 | P285, p. 1 | yes | adjusted | yes | adjusted | "HERTZ SETS FINANCIAL RECORDS FOR FOURTH QUARTER AND FULL YEAR Company provides earnings guidance and outlook for 2013 · Record worldwide revenues for the fourth quarter and full year 2012, up 15.1% (15.5% excluding currency effects), and 8.7% (10.5% excluding currency effects), respectively, year-over-year (“YOY”). · Record fourth quarter adjusted pre-tax margin of 9.2%, and record adjusted pre-tax income(1) of" |
| Q1 FY2013 | P287, p. 1 | yes | adjusted | yes | adjusted | "HERTZ SETS FINANCIAL RECORDS FOR FIRST QUARTER 2013 · Record first quarter worldwide revenues of $2,436.5 million, up 24.3% year-over-year (“YOY”). · Record first quarter worldwide car rental revenues of $2,084.8 million, on record transaction days; worldwide equipment rental revenues increased 16.2% YOY, with an 18.6% rental revenue increase in North America. · U.S. car rental first quarter total RPD" |
| Q2 FY2013 | P289, p. 1 | yes | adjusted | yes | adjusted | "HERTZ SETS FINANCIAL RECORDS FOR SECOND QUARTER 2013 Eight Consecutive Quarters of Record Adjusted Pre-Tax Income · Record second quarter worldwide revenues of $2,714.6 million, up 22.0% year-over-year (“YOY”). · Record second quarter worldwide car rental revenues of $2,329.5 million, on record transaction days; worldwide equipment rental revenues increased 14.7% YOY, with a 17.4% rental revenue increase in North America." |
| Q3 FY2013 | P293, p. 1 | yes | adjusted | yes | adjusted | "HERTZ REPORTS STRONG THIRD QUARTER 2013 Nine Consecutive Quarters of Record Adjusted Pre-Tax Income · Record third quarter worldwide revenues of $3,069.4 million, record adjusted pre-tax income of $519.5 million, and record adjusted diluted earnings per share of $0.73, and up 22.0%, 22.3%, and 15.9% YOY, respectively. · Third quarter GAAP pre-tax income of $328.3 million and GAAP diluted earnings" |
| Q4 FY2013 | P295, p. 1 | yes | adjusted | yes | adjusted | "HERTZ REPORTS FOURTH QUARTER AND FULL YEAR 2013 RESULTS Company announces 2014 revenue and earnings guidance · Record fourth quarter worldwide revenues of $2,556.3 million, up 10.2% over the prior year period. · Fourth quarter adjusted pre-tax income(1) of $186.3 million, versus $210.7 million in the fourth quarter of 2012, and adjusted diluted earnings per share of $0.26 compared with" |

Across the 12 releases: GAAP appears in every headline block and every opening paragraph; the first adjusted measure precedes the first GAAP measure in 10 of 12 headline blocks and in 12 of 12 opening paragraphs; no all-caps title mentions a GAAP measure [P271 to P295, p. 1].

### 4.6 Capitalization and estimates (C5 to C8)

PP&E is on the cost model [P0, header table], so no revaluation effect enters depreciation.

Table 6a. Depreciation, capital spending and estimate changes (decimals unless stated)

| Line | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 | Mark |
|---|---|---|---|---|---|---|
| Depreciation (P&E) / average gross P&E | n/a | 0.0803 | 0.0758 | 0.0727 | 0.0794 | [calc] |
| Fleet depreciation (P1 line) / average gross fleet | n/a | 0.1629 | 0.1527 | 0.1460 | 0.1447 (0.1449 on revised FY2012) | [calc] |
| Fleet depreciation before disposal adjustment (note) / average gross fleet | n/a | 0.1590 | 0.1622 | 0.1528 | 0.1425 | [calc; P16, P45, P74] |
| Disposal adjustment / depreciation before adjustment | 0.0404 | 0.0246 | -0.0584 | -0.0447 | 0.0154 | [calc; P16, P45, P74] |
| Depreciation-rate change effect, car + equipment (USD m) | +19.3 | +22.7 | -18.2 | -130.1 | -39.6 | [calc; P16, p. 125; P45, p. 113; P74, p. 126] |
| Rate change effect / pre-tax income as originally reported | n/m (loss) | n/m (loss) | -0.0561 | -0.2888 | -0.0597 | [calc] |
| Capex (P&E) / depreciation (P&E) | 0.631 | 1.164 | 1.783 | 1.812 | 1.528 | [calc] |
| Net fleet capex / fleet depreciation | 0.768 | 0.515 | 0.886 | 1.203 | 1.241 | [calc] |
| Stated car holding period / useful life range | not in pack | not in pack | 4 to 26 months | 4 to 28 months | 4 to 36 months | [P11, p. 94; P39, p. 81; P68, p. 91] |
| Capitalized internal use software life | not in pack | not in pack | 1 to 15 years | 1 to 15 years | 1 to 10 years | [P11, p. 94; P39, p. 81; P68, p. 91] |
| Capitalized software additions; capitalized contract costs; interest capitalized | not disclosed | not disclosed | not disclosed | not disclosed | not disclosed | [not found: see section 7] |

Table 6b. 2013 path of U.S. car rental depreciation-rate changes and U.S. vehicle disposal results (USD m; negative disposal result = net loss)

| Line | H1 2013 | Q3 2013 | Q4 2013 (derived) | FY2013 | Mark |
|---|---|---|---|---|---|
| U.S. rate change effect on depreciation | -17.3 | -18.0 | -8.9 | -44.2 | [P254, p. 14; P74, p. 126; calc for H1 and Q4] |
| U.S. vehicle disposal result | -9.4 | -11.1 | -27.7 | -48.2 | [P254, p. 14; P74, p. 126; calc for H1 and Q4] |

Q4 2013 in Table 6b is FY2013 (10-K, corrected basis) minus nine months (10-Q, pre-revision basis), so it absorbs any E24 correction to these lines [inf: context sheet, Read first item 2]. In each period of 2013, U.S. rates were reduced while U.S. disposals produced net losses; in FY2012 the reductions (car rental USD -130.6m) came with U.S. disposal gains of USD 100.6m (as reprinted) [P74, p. 126; P45, p. 113].

Reading Table 6: fleet depreciation per dollar of average gross fleet fell in each of the last three years (0.1629 to 0.1447) and net fleet capex per dollar of fleet depreciation rose in each (0.515 to 1.241) [calc]. The FY2012 rate change effect equals 28.9% of FY2012 pre-tax income as originally reported (29.5% of pre-tax income as revised) [calc]. P&E depreciation per dollar of gross P&E moved within 0.0727 to 0.0803 with no trend [calc]. Capitalized software and interest amounts are not disclosed, so C7 ran only as a text search [not found: section 7].

### 4.7 Cash-flow comparisons (C17, C19)

Table 7a. Cash-flow comparisons, annual (USD millions)

| Line | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 | Mark |
|---|---|---|---|---|---|---|
| Income from continuing operations | -111.3 | -30.7 | 195.7 | 243.1 | 346.2 | [P1, IS_A] |
| Cash from operations | 1693.3 | 2208.7 | 2233.3 | 2718.0 | 3589.6 | [P1, CF_A] |
| CFO / income | -15.21 (n/m, loss) | -71.94 (n/m, loss) | 11.41 | 11.18 | 10.37 | [calc] |
| FCF = CFO - capex (P&E) | 1592.6 | 2029.5 | 1951.6 | 2405.2 | 3275.8 | [calc] |
| FCF / income | -14.31 (n/m) | -66.11 (n/m) | 9.97 | 9.89 | 9.46 | [calc] |
| FCF after net fleet capex = FCF - fleet purchases + fleet disposal proceeds | 171.9 | 1107.0 | 347.7 | -82.9 | 241.5 | [calc] |
| FCF after net fleet capex / income | -1.54 (n/m) | -36.06 (n/m) | 1.78 | -0.34 | 0.70 | [calc] |
| Capex (P&E) / depreciation (P&E) | 0.631 | 1.164 | 1.783 | 1.812 | 1.528 | [calc] |
| Fleet purchases / fleet depreciation | 4.069 | 4.716 | 5.225 | 4.648 | 4.212 | [calc] |
| Net fleet capex / fleet depreciation | 0.768 | 0.515 | 0.886 | 1.203 | 1.241 | [calc] |

Table 7b. Cash-flow comparisons, trailing four quarters

| Line | Q4 FY2011 | Q1 FY2012 | Q2 FY2012 | Q3 FY2012 | Q4 FY2012 | Q1 FY2013 | Q2 FY2013 | Q3 FY2013 | Q4 FY2013 | Mark |
|---|---|---|---|---|---|---|---|---|---|---|
| CFO / income | 11.41 | 9.54 | 8.98 | 8.19 | 11.18 | 9.36 | 8.73 | 10.83 | 10.37 | [calc] |
| FCF / income | 9.97 | 8.42 | 8.01 | 7.26 | 9.89 | 8.35 | 7.73 | 9.79 | 9.46 | [calc] |
| FCF after net fleet capex / income | 1.78 | 1.08 | 2.31 | 2.62 | -0.34 | -0.67 | -2.33 | -0.58 | 0.70 | [calc] |
| Capex (P&E) / depreciation (P&E) | 1.78 | 1.84 | 1.78 | 1.87 | 1.81 | 1.75 | 1.80 | 1.67 | 1.53 | [calc] |
| Fleet purchases / fleet depreciation | 5.22 | 5.37 | 4.87 | 4.56 | 4.65 | 4.75 | 4.72 | 4.73 | 4.21 | [calc] |
| Net fleet capex / fleet depreciation | 0.89 | 1.04 | 0.86 | 0.76 | 1.20 | 1.33 | 1.53 | 1.38 | 1.24 | [calc] |

Reading Table 7: cash from operations runs at about ten times income from continuing operations in every positive-income year (11.41, 11.18, 10.37) and free cash flow after P&E capex at about nine to ten times (9.97, 9.89, 9.46) [calc], because fleet depreciation is added back in operating cash flow while fleet purchases are investing cash flows [P66, pp. 80 to 81; inf]. Both ratios moved down together into FY2013, the lowest of the three positive-income years [calc]. The measure that moved most is free cash flow after net fleet capex: 1.78 times income in FY2011, -0.34 in FY2012 and 0.70 in FY2013 [calc]. Capitalized software is not a separate cash-flow line [P1, CF_A blank; P66, pp. 80 to 81], so it is inside "property and equipment expenditures" if it exists [inf: P68, p. 91 lists it among property and equipment lives].

## 5. Text found

Line numbers refer to the pack text file and are given where the page marker is "unnumbered" or a page is long.

**Step 5 (adjusted measures)**

1. Corporate EBITDA footnote, repeated in every release from Q1 FY2011 to Q4 FY2013: "As defined in the credit agreements for the senior credit facilities, Corporate EBITDA excludes the impact of extraordinary, unusual or non-recurring gains or losses or charges or credits." [P295, Table 7, p. 3 marker, line 675; P271, p. 13, line 508]. The table beneath it, headed "EXTRAORDINARY, UNUSUAL OR NON-RECURRING ITEMS", lists "Restructuring charges" and "Acquisition related costs" in every quarter [P271 to P295, Corporate EBITDA table; calc, Table 5b].
2. Definition in the releases: "Adjusted pre-tax income is calculated as income before income taxes plus non-cash purchase accounting charges, non-cash debt charges relating to the amortization of debt financing costs and debt discounts and certain one-time charges and non-operational items." [P271, p. 15, line 654]
3. Definition in the filed FY2013 10-K: "Adjusted pre-tax income is calculated as income before income taxes plus certain non-cash purchase accounting charges, debt-related charges relating to the amortization and write-off of debt financing costs and debt discounts and certain one-time charges and nonoperational items." [P62, p. 50, note (c)]. The same measure is the segment measure in Note 11 [P77, p. 131].
4. Restructuring related charges, FY2013 10-K: "Represents incremental costs incurred directly supporting our business transformation initiatives." [P77, p. 135, footnote (4)]
5. Relocation: "For the year ended December 31, 2013, $21.9 million of costs related to the relocation of our corporate headquarters to Estero, Florida were recorded within restructuring charges." [P62, p. 44; P80, p. 140]. "We anticipate that our expenditures related to the move of our corporate headquarters to Estero, Florida for employee relocation, severance and associated costs will be in the range of $40 million to $45 million to be incurred over the next two years." [P62, p. 65]. The segment reconciliation adjusts out "Relocation costs | (7.8)" for 2013 [P77, p. 134].
6. Integration expenses: "In 2013, primarily represents Dollar Thrifty integration related expenses." [P77, p. 135, footnote (7)]. The Q1 FY2013 release that introduced the category gives no definition; its only related text is the CEO's remark on "integration and synergy progress" [P287, p. 2].
7. Q4 FY2012 debt charges: "(d) Represents non-cash debt charges relating to the amortization and write off of deferred debt financing costs and debt discounts of $17.3 million and $22.4 million for the three months ended December 31, 2012 and 2011, respectively. ... Also includes $17.5 million of pre-acquisition interest and commitment fee expenses for interim financing associated with the Dollar Thrifty acquisition for the three and twelve months ended December 31, 2012." [P285, p. 10, line 291]
8. Q4 FY2013 relabel: the line reads "Debt-related charges" [P295, p. 2, line 36] and "(d) Represents debt-related charges relating to the amortization of deferred debt financing costs and debt discounts." [P295, Table 6, line 315]. The Q3 FY2013 release still reads "Non-cash debt charges" [P293, p. 2, line 34].
9. Tax rate in adjusted net income: "Assumed provision for income taxes at 35% in 2013 and 34% in 2012" [P287, p. 2, line 41]; earlier "(34% in 2012 and 2011)" [P285, p. 20, line 732]. Stated basis: "The normalized income tax rate is management’s estimate of our long-term tax rate." [P295, line 817]
10. Adjusted EPS numerator: "(a) We had a change in policy in Q1 2013 with respect to settling the conversion of our 5.25% Convertible Senior Notes due June 2014." [P295, p. 2, line 48] (context sheet E13).
11. Q2 FY2013 release, Table 1 reports "Acquisition related costs | 9.1 | 4.5" (Q2 2013 and Q2 2012) [P289, p. 2, line 41], and the Q2 FY2012 release reported "Acquisition related costs | 4.5 | 6.1" [P281, p. 2, line 38]; the same Q2 FY2013 release's Table 5 puts the Q2 2012 amount of 4.5 on the row labelled "Integration expensess (d)" and none on "Acquisition related costs (d)" [P289, p. 11, lines 374 to 375], while its six-month 2012 column shows acquisition related costs of 11.4, which equals Q1 FY2012's 6.9 plus 4.5 [P289, p. 11, line 405; calc].
12. Q2 FY2013 release, Table 5 row label: "Other unusual/non-recurring (c)" for USD 5.4m [P289, p. 11, line 377]; the Q3 FY2013 release uses the same label [P293, p. 14, line 470].
13. Q3 FY2013 release: "Note: Certain adjustments have been reclassified to conform with current period presentation." [P293, p. 10, line 265]. Relocation costs for nine months are 4.4 against 3.9 for Q3, so 0.5 of first-half relocation cost sat under another label in the Q1 and Q2 releases [P293, line 491; calc].
14. New categories, Q3 FY2013: "(a) Related to Franchise Services of North America and its subsidiary, Simply Wheelz, LLC as disclosed below." and "(b) Primarily represents expenses related to the loss on conversion of the convertible senior notes as disclosed below." [P293, p. 2, lines 48 and 50]. Q4 FY2012 "Other": "(g) Primarily represents expenses related to the withdrawal from a multiemployer pension plan of $23.2 million, litigation accrual of $14.0 million and expenses associated with the impact of Hurricane Sandy of $7.9 million." [P285, p. 14, line 503]

**Step 6 (capitalization and estimates)**

15. FY2013 depreciation note: "These depreciation rate changes in our U.S. car rental operations from previous quarters resulted in net decreases of $44.2 million, $139.4 million and $26.7 million in depreciation expense for the years ended December 31, 2013, 2012 and 2011, respectively." [P74, p. 126]
16. Same note: "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. for the years ended December 31, 2013, 2012 and 2011." [P74, p. 126]
17. Same note, disposal results: "included net losses of $48.2 million, and net gains of $100.6 million and $114.9 million, respectively, on the disposal of vehicles used in our U.S. car rental operations" and "The loss on vehicle sales in our car rental operations was primarily due to a combination of declining residual values from falling demand for used vehicles and timing of sales of revenue earning equipment in our car rental operations." [P74, p. 126]
18. FY2013 MD&A, U.S. car rental: "The increase was primarily attributable to an increase in average fleet due to the Recent Acquisitions and a deterioration in the used vehicle residual values." [P62, p. 54]
19. FY2012 depreciation note: "The cumulative effect of the reduction in rates was indicative of the strong residual values experienced in the U.S. for the years ended December 31, 2012 and 2011." [P45, p. 113]
20. FY2011 depreciation note: "These depreciation rate changes resulted in a net decrease of $13.8 million and increases of $19.1 million and $13.2 million in depreciation expense for the years ended December 31, 2011, 2010 and 2009, respectively." [P16, p. 125]
21. Q3 FY2013 10-Q: "The depreciation rate changes in our U.S. car rental operations from previous quarters resulted in net decreases of $18.0 million and $35.3 million, respectively, for the three-month and nine-month periods ended September 30, 2013." [P254, p. 14]. Q2 FY2013 10-Q: "Prospective changes include the impact of car sales channel diversification and acceleration of our retail sales expansion." [P234, p. 14]
22. Lives and holding periods, by year. FY2011: "The provisions for depreciation and amortization are computed on a straight-line basis over the estimated useful lives of the respective assets, or in the case of revenue earning equipment over the estimated holding period, as follows:" with "Cars | 4 to 26 months", "Other equipment | 24 to 108 months", "Buildings | 3 to 50 years", "Capitalized internal use software | 1 to 15 years", "Other intangible assets | 3 to 20 years" [P11, p. 94]. FY2012: "Revenue earning equipment is stated at cost, net of related discounts. Useful lives are as follows:" with "Cars | 4 to 28 months", "Other equipment | 24 to 108 months"; P&E lives unchanged from FY2011 [P39, p. 81]. FY2013: "Revenue earning equipment is stated at cost, net of related discounts. Holding periods are as follows:" with "Cars | 4 to 36 months", "Other equipment | 24 to 108 months", "Buildings | 5 to 50 years", "Capitalized internal use software | 1 to 10 years", "Other intangible assets | 3 to 10 years" [P68, p. 91].
23. Residual values, all three years: "We also estimate the residual value of the applicable revenue earning equipment at the expected time of disposal." [P11, p. 94; P39, p. 81; P68, p. 91]. FY2013 MD&A: "Depreciation rates are adjusted prospectively through the remaining expected life." [P62, p. 45]
24. Donlen: "These leases contain provisions whereby we have a contracted residual value guaranteed to us by the lessee, such that we do not experience any gains or losses on the disposal of these vehicles." [P68, p. 91]
25. C6: no hit for "change in estimate", "change in accounting estimate" or "changes in estimate" in any of the 298 text files [calc, search]. The public liability reserve text describes actuarial method only: "Reserve requirements are based on actuarial evaluations of historical accident claim experience and trends, as well as future projections of ultimate losses, expenses, premiums and administrative costs." [P68, p. 92, "Public Liability and Property Damage"]

**Step 7 (cash-flow classification)**

26. "Interest (net of amounts capitalized) | $651.0 | $560.0 | $640.6" [P66, p. 81]; "Cash paid for interest during the year ended December 31, 2013, was $651.0 million, net of amounts capitalized." [P62, p. 66]
27. "For the three months ended March 31, 2010, we have revised net cash provided by operating activities and net cash used in investing activities within our consolidated statement of cash flows due to a gross-up of cash lease payments relating to our revenue earning equipment in the non-cash add back previously included in depreciation of revenue earning equipment and proceeds from disposal of revenue earning equipment." [P91, p. 7] (context sheet E1)
28. Parent-only statements: "The classification of these amounts have been corrected so that they are presented as cash flows from investing activities." [P37, p. 138] (context sheet E12)
29. Non-cash supplemental lines: "Sales of revenue earning equipment included in receivables | 357.3 | 618.6 | 620.7" and "Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1 | $247.0 | $153.6" [P66, p. 81]
30. Company free cash flow: "Free cash flow(1) for the year ended December 31, 2013 was $448.7 million an increase of $293.6 million compared to the same period last year." [P295, p. 2] and "(1) 2012 free cash flow excludes certain DTG acquisition related items of approximately $129.6 million as previously disclosed." [P295, Table 7, line 599]
31. "Securitization" appears in 470 lines in 75 files, as the names of fleet debt facilities (for example "European Securitization") inside Debt [calc, search; P71]. "Beneficial interest" appears only as: "The notes issued by HFLF are ultimately backed by a special unit of beneficial interest in a pool of leases and the related vehicles." [P71, p. 110], a debt facility, not a receivable sale.

## 6. Ledger rows

ID convention: step, checklist row, sequence. The checklist that defines the rows is not in the pack, so the row assignment is an assumption: C1 gap, C2 recurring label, C3 new categories and definition changes, C4 prominence, C5 depreciation and capital-spending ratios, C6 estimate changes near reserves, C7 capitalized costs and interest, C8 statements of lives and residual values [inf: F3 prompt, steps 5 and 6].

| ID | Item | Period | Evidence | Locator | Benign reading | Adverse reading | Context | Resolving disclosure | Priority | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| F3-C8-01 | C8 Fleet depreciation rates and residual values, stated inconsistency | FY2013 | Note 8: U.S. rate changes "resulted in net decreases of $44.2 million" in 2013 and "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. for the years ended December 31, 2013, 2012 and 2011." Same note: U.S. vehicle disposals had "net losses of $48.2 million" in 2013, due to "declining residual values from falling demand for used vehicles"; MD&A cites "a deterioration in the used vehicle residual values". 2013 path: U.S. rate reductions H1 -17.3, Q3 -18.0, Q4 -8.9 against U.S. disposal results -9.4, -11.1, -27.7 [calc] | P74, p. 126; P62, p. 54; P254, p. 14; P234, pp. 13 to 14 | The reductions were set in earlier quarters ("from previous quarters") on the residual evidence then available and on expected gains from new sales channels ("car sales channel diversification and acceleration of our retail sales expansion", P234); losses arose on cars sold after residuals weakened late in the year, and rates are "adjusted prospectively" (P62, p. 45), so the two statements can describe different parts of the year | Depreciation rates were lowered in every 2013 period while cars sold realized less than book value, so the book value of cars still held at 31 December 2013 may exceed what they will realize and cost may reach later periods as disposal losses, which enter depreciation on sale | E22 (rate changes every year); E9 (holding-period optimization with Dollar Thrifty); E24 (fleet cost revised); Q4 2013 derived on mixed bases (context sheet, Read first item 2) | Q4 2013 rate-change and disposal detail, age and residual assumptions of the year-end fleet: not in pack (searched P74, P62, P254, P295, P296) | P1 |  |
| F3-C5-01 | C5 Fleet depreciation rate down while fleet reinvestment up | FY2010 to FY2013 | Fleet depreciation / average gross fleet 0.1629, 0.1527, 0.1460, 0.1447, lowest in FY2013 and down three years running; net fleet capex / fleet depreciation 0.515, 0.886, 1.203, 1.241, highest in FY2013 and up three years running; rate-change effect -18.2, -130.1, -39.6 (FY2011 to FY2013), FY2012 equal to 28.9% of pre-tax income as originally reported [calc]. Triggers (a) and (b) | P1, IS_A, BS_A, CF_A; P16, p. 125; P45, p. 113; P74, p. 126 | Fleet growth and acquisitions (Donlen lease vehicles with contracted residuals, Dollar Thrifty) raise gross fleet and purchases; strong 2011 to 2012 residuals and longer holding periods justify lower rates; on the revised FY2012 base the FY2013 rate (0.1449) is level with FY2012 as revised (0.1448) [calc] | Each year's estimate change moved depreciation down while 2013 disposal results turned to losses, so reported fleet cost may run below eventual realized cost and the gap would surface later | E2, E9, E16 (fleet acquired); E22 (rate changes); E24 | Fleet mix (program versus non-program, Donlen share) and average holding period by year: not found in Notes 2 and 8 or MD&A depreciation sections searched | P2 |  |
| F3-C8-02 | C8 Stated car holding-period range lengthened; other stated lives changed | FY2011 to FY2013 | "Cars \| 4 to 26 months" (FY2011), "Cars \| 4 to 28 months" under "Useful lives are as follows:" (FY2012), "Cars \| 4 to 36 months" under "Holding periods are as follows:" (FY2013); FY2013 also "Capitalized internal use software \| 1 to 10 years" (was 1 to 15), "Buildings \| 5 to 50 years" (was 3 to 50), "Other intangible assets \| 3 to 10 years" (was 3 to 20). No change-in-estimate wording in any of 298 text files [calc, search] | P11, p. 94; P39, p. 81; P68, p. 91 | The ranges describe the fleet and assets in place (Dollar Thrifty vehicles, longer-held cars) rather than a change in estimate; the software and intangible ranges shortened, which adds expense; Note 8 quantifies the rate changes | A longer maximum holding period lowers monthly depreciation per car and its effect is not quantified apart from the rate changes; changes are prospective, so the depreciation series breaks without restatement | E9 ("optimization of fleet holding periods related to the integration of Dollar Thrifty", P74); E22 | Depreciation effect of the holding-period extension: not in pack (searched P74, P68, P62, P254) | P2 |  |
| F3-C2-01 | C2 Recurring adjustments labelled non-recurring or one-time | Q1 FY2011 to Q4 FY2013 | Restructuring adjusted out in 16 of 16 quarters and acquisition related costs in 15 of 16 (Q1 FY2010 to Q4 FY2013); restructuring 49.1 (FY2012) to 100.2 (FY2013) [calc]; both listed each quarter under "EXTRAORDINARY, UNUSUAL OR NON-RECURRING ITEMS"; definition "certain one-time charges" in releases and the filed 10-K; 10-K expects relocation spending "over the next two years" while "Relocation costs" are adjusted out | P271 to P295, INCOME MEASUREMENTS and Corporate EBITDA tables; P62, pp. 50 and 65; P77, pp. 134 to 135 | The non-recurring wording is the credit-agreement definition of Corporate EBITDA ("As defined in the credit agreements for the senior credit facilities"), not management's description; adjusted pre-tax income is the ASC 280 segment measure; restructuring is disclosed every quarter as a multi-year programme ("incremental costs incurred directly supporting our business transformation initiatives") | Charges present every quarter and doubling in FY2013 are presented as one-time or non-recurring, so adjusted pre-tax income may overstate the recurring run-rate by those amounts; in filed documents Item 10(e) bars the non-recurring label for charges that occurred in the prior two years or are reasonably likely in the next two | E9 (integration), E10; restructuring and relocation are not on the context sheet | Management's basis for the one-time label in the filed MD&A (P62, p. 50 note (c)); Item 10(e)(1)(ii)(B) text not in pack | P2 |  |
| F3-C3-01 | C3 Debt-charge label and definition changed; tax rate changed | Q4 FY2012 to Q4 FY2013 | Q4 FY2012 "non-cash debt charges" "Also includes $17.5 million of pre-acquisition interest and commitment fee expenses for interim financing"; from Q4 FY2013 the line is "Debt-related charges", defined as "debt-related charges relating to the amortization of deferred debt financing costs and debt discounts"; normalized tax rate 34% (2012) to 35% (2013) | P285, p. 10, line 291; P295, p. 2, line 36 and line 315; P287, p. 2, line 41; P295, line 817 | The new label fits a line that had included a cash item; the tax rate is management's "estimate of our long-term tax rate" and each year is shown at its own rate | A line labelled non-cash included cash interest and fees in Q4 FY2012, then the label changed with no stated reason; the rate change shifts adjusted net income between years | E13 (EPS numerator policy), E14 (RPD definition); the relabel is not on the context sheet | Explanation or recast of the relabel: not found in P295, P296 ("non-cash debt", "previously", "formerly", "renamed", "conform", "reclassif") | P3 |  |
| F3-C3-02 | C3 Q2 FY2012 amount carried under two categories in one release | Q2 FY2013 | Table 1 shows Q2 2012 acquisition related costs of 4.5 (as in the Q2 FY2012 release); Table 5 of the same release puts that 4.5 on "Integration expensess (d)" and none on acquisition related costs, while its six-month 2012 column keeps 11.4 (6.9 + 4.5 [calc]) under acquisition related costs; Q2 2013 acquisition plus integration costs are 18.3 in Table 1 and 25.3 in the Corporate EBITDA non-recurring table [calc] | P289, p. 2, line 41; p. 11, lines 374 to 375 and 405; p. 13, line 547; P281, p. 2, line 38 | A labelling slip in a furnished release with no effect on the adjusted total; the two reconciliations serve different measures (adjusted pre-tax income and the credit-agreement Corporate EBITDA), so category amounts can differ | Boundaries between acquisition, integration and restructuring costs are not stable across tables, which makes growth in any one category hard to track | E9 | Reconciliation of category amounts between the two tables: not found in P289 | P3 |  |
| F3-C3-03 | C3 New adjustment categories | Q4 FY2012 to Q4 FY2013 | First appearances: Other (Q4 FY2012), Integration expenses (Q1 FY2013), Relocation costs and Impairment charges and other (Q3 FY2013) [calc]; row label "Other unusual/non-recurring (c)" (Q2 and Q3 FY2013); FY2013 amounts 40.0, 7.8, 44.0 and 50.7; "Certain adjustments have been reclassified to conform with current period presentation"; 0.5 of first-half relocation cost sat under another label [calc] | P285, p. 2; P287, p. 2; P293, pp. 2, 10, 14; P295, p. 5 | Each new category matches a disclosed event (Dollar Thrifty integration, headquarters move, Simply Wheelz bankruptcy, convertible note conversion, pension withdrawal and Hurricane Sandy), and the prior periods had none | The set of excluded items widened in FY2013, raising the gap between adjusted and GAAP pre-tax income; Integration and Relocation were not defined in the releases that introduced them | E9, E10, E13 | Definitions in the introducing releases: not found in P287, P293; given later in the FY2013 10-K (P77, p. 135; P62, pp. 44 and 65) | P3 |  |
| F3-C4-01 | C4 Prominence: adjusted measures lead | Q1 FY2011 to Q4 FY2013 | First adjusted measure precedes the first GAAP measure in 10 of 12 headline blocks and 12 of 12 opening paragraphs; GAAP present in all 12 headline blocks and opening paragraphs [calc]; titles such as "Nine Consecutive Quarters of Record Adjusted Pre-Tax Income" | P271 to P295, p. 1 (first 60 words in Table 5c); P293, p. 1 | Every release states GAAP pre-tax income and EPS in the bullets and first paragraph with full reconciliations, and the adjusted measure is the company's segment measure | The ordering gives adjusted figures more prominence than GAAP figures; releases furnished under Item 2.02 are subject to the equal-or-greater-prominence requirement [unverified: rule text not in pack] | none | Item 10(e)(1)(i)(A) and Form 8-K Item 2.02 instruction text; any SEC comment correspondence: not in pack | P3 |  |
| F3-B4-01 | B4 GMI rising for three pairs | FY2013 / FY2012 | GMI 0.8190, 0.8484, 0.9559, 0.9942 (1.0001 against FY2012 as revised); cost-line margin 0.1529, 0.1867, 0.2201, 0.2302, 0.2316 [calc]. Triggers (a) and (b) | P1, IS_A and EXTRA (direct operating; depreciation of revenue earning equipment and lease charges) | Margin rose every year; GMI approaches 1 from below as recovery gains level off | Margin gains have flattened while fleet depreciation-rate reductions (130.1 in FY2012, 39.6 in FY2013) were part of the cost line, so the margin level partly rests on estimate changes | E22, E24 (vendor incentives moved into fleet cost), E9 | Cost-line margin excluding rate changes and disposal adjustments: inputs in pack (Note 8), not computed here | P3 |  |
| F3-B1-01 | B1/B2 Balance-sheet and cash-flow accruals diverge; residuals not traced | FY2010 to FY2013 | Balance-sheet minus cash-flow accrual numerator -180.4, 414.8, 600.0, 726.6 (-0.0108 to 0.0304 of average total assets); FY2013 receivables line differs by 408.7, of which 260.0 lower fleet-sale receivables and 45.9 provision, leaving 102.8 (118.5 after property-sale receivables) not traced; prepaid and other 205.7; accrued liabilities -101.0 [calc] | P1, BS_A, CF_A, EXTRA; P66, pp. 75 and 80 to 81 | Acquisitions and de-consolidation (E2, E9, E15, E16), fleet-related non-cash investing balances, restricted cash (investing) and deferred taxes (non-current) sit in the balance-sheet measure and not in operating cash flow; FY2010 payables difference lines up with fleet purchases held in payables | Part of the FY2013 movement in receivables and accrued liabilities is not traced to a disclosed line, so some operating balance changes may sit outside operating cash flow | E2, E9, E10, E15, E16; tie-out W1 | Receivables and accrued-liability rollforwards; balances removed with the China entities: not found in P70, P66 | P3 |  |
| F3-C17-01 | C17 Cash from operations and free cash flow relative to income at series low | FY2013 | CFO / income 11.41, 11.18, 10.37; FCF / income 9.97, 9.89, 9.46 (FY2011 to FY2013; FY2009 and FY2010 were losses); FCF after net fleet capex / income 1.78, -0.34, 0.70 [calc]. Trigger (a) | P1, CF_A and IS_A | Ratios near 10 are structural: fleet depreciation is an operating add-back and fleet purchases are investing; income grew faster than cash flow in the highest-income year, with deferred tax up to 241.3 | Free cash flow after fleet reinvestment has been below income since FY2012 and was negative in FY2012, so reported income is not matched by cash after fleet replacement | E9; E24 (FY2012 CFO revised -8.3); tie-out W1 | Fleet financing flows and program-car repurchase receipts: partly in P295 Table 7 | P3 |  |
| F3-C7-01 | C7 Interest capitalized referenced but not quantified | FY2011 to FY2013 | "Interest (net of amounts capitalized)" in each cash flow statement and "net of amounts capitalized" in MD&A; "capitalized interest", "interest capitalized" and "construction in progress" return 0 hits in 298 files [calc, search] | P66, p. 81; P62, p. 66; P9, p. 90; P37, p. 78 | Capitalized interest is nil or immaterial and the caption is standard wording | If interest is capitalized in amounts that matter, part of interest cost is deferred to the balance sheet without a stated amount | none | Interest incurred and capitalized by year (ASC 835-20 disclosure) [unverified: standard not in pack]; not in pack | P3 |  |
| F3-C17-02 | C17 Company free cash flow excludes DTG items in FY2012 | FY2012 and FY2013 | "(1) 2012 free cash flow excludes certain DTG acquisition related items of approximately $129.6 million as previously disclosed."; FY2013 free cash flow "$448.7 million an increase of $293.6 million" | P295, p. 2 and Table 7, line 599 | One-off acquisition-related cash items were removed so the years compare on operating terms, and the exclusion is footnoted | The direction of the excluded items is not stated, so the effect on the reported FY2013 increase cannot be read from the release; the company measure also differs from the step 7 measure | E9 | Composition of the 129.6: not found in P295, P296 | P4 |  |
| F3-B4-02 | B4 SGI highest in series | FY2013 / FY2012 | SGI 1.1941 against 1.0649 to 1.0973 in earlier pairs [calc]. Trigger (a) | P1, IS_A | Full year of Dollar Thrifty in FY2013 against 43 days in FY2012 | Post-acquisition growth is the setting in which the SGI term was estimated as a pressure indicator | E9, E10, E15 | Revenue growth excluding Dollar Thrifty: release attributes U.S. growth "primarily due to Dollar Thrifty" (P295, p. 1); amount not found | P4 |  |
| F3-B4-03 | B4 SGAI lowest in series | FY2013 / FY2012 | SGAI 0.9051 (0.8846 against FY2012 as revised); SG&A / revenue 0.1048 (FY2012; 0.1073 revised) to 0.0949 (FY2013) [calc]. Trigger (a): lower SGAI raises M | P1, IS_A; P66, p. 76 | Dollar Thrifty synergies and scale; FY2012 SG&A carried Dollar Thrifty acquisition costs | SG&A fell as a share of revenue in a period when costs were reclassified between SG&A and fleet cost (E24) | E9, E24 | SG&A excluding acquisition and integration costs by year: partly in release Table 5 (P285, P295) | P4 |  |
| F3-B5-01 | B5 F-score above 1.0 on workbook mapping; soft assets rising | FY2011 to FY2013 | F-score 1.768, 1.850 (1.8497), 1.766; soft assets 0.7959, 0.8764, 0.9154, 0.9212 (FY2010 to FY2013), highest in FY2013 and up three years; largest contributions soft assets (+1.82 in FY2013) and issuance (+1.029); fleet in PP&E gives 0.573, 0.620, 0.566 [calc]. Triggers (a) and (b) on soft assets | P1, BS_A and CF_A | The rental fleet (0.55 to 0.58 of assets) is outside the P1 PP&E line, and goodwill and intangibles rose from 0.1672 to 0.2308 of assets with Dollar Thrifty; issuance is 1 for a company that refinances fleet debt continuously | A larger share of assets rests on valuation estimates (goodwill, intangibles, fleet residuals), mostly from acquisitions | E2, E9, E21 | Goodwill and trade-name impairment testing (Note 3, in pack; F4) | P4 |  |
| F3-B6-01 | B6 Cash sales growth highest in series | FY2013 | Change in cash sales 0.0674, 0.0886, 0.2737 against FY2013 revenue growth 0.1941 and receivables growth -0.1982; FY2013 cash-flow accruals -0.1355 and RSST 0.0156 [calc]. Trigger (a) | P1, IS_A, BS_A, EXTRA | Fleet-sale receivables (investing) fell 260.0, Dollar Thrifty contributed a full year and the China entities left the balance sheet; accruals are low, so the step 4 pairing with high accruals does not arise | The part of the receivables decline not traced to a line (F3-B1-01) would lift cash sales without a cash counterpart in operations | E9, E15 | Receivables rollforward (F2, A1 to A8) | P4 |  |
| F3-C19-01 | C19 Cash-flow classification revisions for fleet lease payments | Q1 2010 to Q3 2010 comparatives | "we have revised net cash provided by operating activities and net cash used in investing activities ... due to a gross-up of cash lease payments relating to our revenue earning equipment"; parent-only return of capital moved to investing; amounts for the gross-up not stated | P91, p. 7; P131 (Q3 2011 10-Q Note 2); P37, p. 138 | Presentation corrections that the company disclosed when made | Classification of fleet-related cash between operating and investing was corrected more than once, so operating cash flow trends across 2010 may include classification effects | E1, E12, E17 (F1-C15-3) | Amounts of the gross-up: not found in P91, P131 | P4 |  |

```csv
ID,Item,Period,Evidence,Locator,Benign reading,Adverse reading,Context,Resolving disclosure,Priority,Verdict
F3-C8-01,"C8 Fleet depreciation rates and residual values, stated inconsistency",FY2013,"Note 8: U.S. rate changes ""resulted in net decreases of $44.2 million"" in 2013 and ""The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. for the years ended December 31, 2013, 2012 and 2011."" Same note: U.S. vehicle disposals had ""net losses of $48.2 million"" in 2013, due to ""declining residual values from falling demand for used vehicles""; MD&A cites ""a deterioration in the used vehicle residual values"". 2013 path: U.S. rate reductions H1 -17.3, Q3 -18.0, Q4 -8.9 against U.S. disposal results -9.4, -11.1, -27.7 [calc]","P74, p. 126; P62, p. 54; P254, p. 14; P234, pp. 13 to 14","The reductions were set in earlier quarters (""from previous quarters"") on the residual evidence then available and on expected gains from new sales channels (""car sales channel diversification and acceleration of our retail sales expansion"", P234); losses arose on cars sold after residuals weakened late in the year, and rates are ""adjusted prospectively"" (P62, p. 45), so the two statements can describe different parts of the year","Depreciation rates were lowered in every 2013 period while cars sold realized less than book value, so the book value of cars still held at 31 December 2013 may exceed what they will realize and cost may reach later periods as disposal losses, which enter depreciation on sale","E22 (rate changes every year); E9 (holding-period optimization with Dollar Thrifty); E24 (fleet cost revised); Q4 2013 derived on mixed bases (context sheet, Read first item 2)","Q4 2013 rate-change and disposal detail, age and residual assumptions of the year-end fleet: not in pack (searched P74, P62, P254, P295, P296)",P1,
F3-C5-01,C5 Fleet depreciation rate down while fleet reinvestment up,FY2010 to FY2013,"Fleet depreciation / average gross fleet 0.1629, 0.1527, 0.1460, 0.1447, lowest in FY2013 and down three years running; net fleet capex / fleet depreciation 0.515, 0.886, 1.203, 1.241, highest in FY2013 and up three years running; rate-change effect -18.2, -130.1, -39.6 (FY2011 to FY2013), FY2012 equal to 28.9% of pre-tax income as originally reported [calc]. Triggers (a) and (b)","P1, IS_A, BS_A, CF_A; P16, p. 125; P45, p. 113; P74, p. 126","Fleet growth and acquisitions (Donlen lease vehicles with contracted residuals, Dollar Thrifty) raise gross fleet and purchases; strong 2011 to 2012 residuals and longer holding periods justify lower rates; on the revised FY2012 base the FY2013 rate (0.1449) is level with FY2012 as revised (0.1448) [calc]","Each year's estimate change moved depreciation down while 2013 disposal results turned to losses, so reported fleet cost may run below eventual realized cost and the gap would surface later","E2, E9, E16 (fleet acquired); E22 (rate changes); E24","Fleet mix (program versus non-program, Donlen share) and average holding period by year: not found in Notes 2 and 8 or MD&A depreciation sections searched",P2,
F3-C8-02,C8 Stated car holding-period range lengthened; other stated lives changed,FY2011 to FY2013,"""Cars | 4 to 26 months"" (FY2011), ""Cars | 4 to 28 months"" under ""Useful lives are as follows:"" (FY2012), ""Cars | 4 to 36 months"" under ""Holding periods are as follows:"" (FY2013); FY2013 also ""Capitalized internal use software | 1 to 10 years"" (was 1 to 15), ""Buildings | 5 to 50 years"" (was 3 to 50), ""Other intangible assets | 3 to 10 years"" (was 3 to 20). No change-in-estimate wording in any of 298 text files [calc, search]","P11, p. 94; P39, p. 81; P68, p. 91","The ranges describe the fleet and assets in place (Dollar Thrifty vehicles, longer-held cars) rather than a change in estimate; the software and intangible ranges shortened, which adds expense; Note 8 quantifies the rate changes","A longer maximum holding period lowers monthly depreciation per car and its effect is not quantified apart from the rate changes; changes are prospective, so the depreciation series breaks without restatement","E9 (""optimization of fleet holding periods related to the integration of Dollar Thrifty"", P74); E22","Depreciation effect of the holding-period extension: not in pack (searched P74, P68, P62, P254)",P2,
F3-C2-01,C2 Recurring adjustments labelled non-recurring or one-time,Q1 FY2011 to Q4 FY2013,"Restructuring adjusted out in 16 of 16 quarters and acquisition related costs in 15 of 16 (Q1 FY2010 to Q4 FY2013); restructuring 49.1 (FY2012) to 100.2 (FY2013) [calc]; both listed each quarter under ""EXTRAORDINARY, UNUSUAL OR NON-RECURRING ITEMS""; definition ""certain one-time charges"" in releases and the filed 10-K; 10-K expects relocation spending ""over the next two years"" while ""Relocation costs"" are adjusted out","P271 to P295, INCOME MEASUREMENTS and Corporate EBITDA tables; P62, pp. 50 and 65; P77, pp. 134 to 135","The non-recurring wording is the credit-agreement definition of Corporate EBITDA (""As defined in the credit agreements for the senior credit facilities""), not management's description; adjusted pre-tax income is the ASC 280 segment measure; restructuring is disclosed every quarter as a multi-year programme (""incremental costs incurred directly supporting our business transformation initiatives"")","Charges present every quarter and doubling in FY2013 are presented as one-time or non-recurring, so adjusted pre-tax income may overstate the recurring run-rate by those amounts; in filed documents Item 10(e) bars the non-recurring label for charges that occurred in the prior two years or are reasonably likely in the next two","E9 (integration), E10; restructuring and relocation are not on the context sheet","Management's basis for the one-time label in the filed MD&A (P62, p. 50 note (c)); Item 10(e)(1)(ii)(B) text not in pack",P2,
F3-C3-01,C3 Debt-charge label and definition changed; tax rate changed,Q4 FY2012 to Q4 FY2013,"Q4 FY2012 ""non-cash debt charges"" ""Also includes $17.5 million of pre-acquisition interest and commitment fee expenses for interim financing""; from Q4 FY2013 the line is ""Debt-related charges"", defined as ""debt-related charges relating to the amortization of deferred debt financing costs and debt discounts""; normalized tax rate 34% (2012) to 35% (2013)","P285, p. 10, line 291; P295, p. 2, line 36 and line 315; P287, p. 2, line 41; P295, line 817","The new label fits a line that had included a cash item; the tax rate is management's ""estimate of our long-term tax rate"" and each year is shown at its own rate","A line labelled non-cash included cash interest and fees in Q4 FY2012, then the label changed with no stated reason; the rate change shifts adjusted net income between years","E13 (EPS numerator policy), E14 (RPD definition); the relabel is not on the context sheet","Explanation or recast of the relabel: not found in P295, P296 (""non-cash debt"", ""previously"", ""formerly"", ""renamed"", ""conform"", ""reclassif"")",P3,
F3-C3-02,C3 Q2 FY2012 amount carried under two categories in one release,Q2 FY2013,"Table 1 shows Q2 2012 acquisition related costs of 4.5 (as in the Q2 FY2012 release); Table 5 of the same release puts that 4.5 on ""Integration expensess (d)"" and none on acquisition related costs, while its six-month 2012 column keeps 11.4 (6.9 + 4.5 [calc]) under acquisition related costs; Q2 2013 acquisition plus integration costs are 18.3 in Table 1 and 25.3 in the Corporate EBITDA non-recurring table [calc]","P289, p. 2, line 41; p. 11, lines 374 to 375 and 405; p. 13, line 547; P281, p. 2, line 38","A labelling slip in a furnished release with no effect on the adjusted total; the two reconciliations serve different measures (adjusted pre-tax income and the credit-agreement Corporate EBITDA), so category amounts can differ","Boundaries between acquisition, integration and restructuring costs are not stable across tables, which makes growth in any one category hard to track",E9,Reconciliation of category amounts between the two tables: not found in P289,P3,
F3-C3-03,C3 New adjustment categories,Q4 FY2012 to Q4 FY2013,"First appearances: Other (Q4 FY2012), Integration expenses (Q1 FY2013), Relocation costs and Impairment charges and other (Q3 FY2013) [calc]; row label ""Other unusual/non-recurring (c)"" (Q2 and Q3 FY2013); FY2013 amounts 40.0, 7.8, 44.0 and 50.7; ""Certain adjustments have been reclassified to conform with current period presentation""; 0.5 of first-half relocation cost sat under another label [calc]","P285, p. 2; P287, p. 2; P293, pp. 2, 10, 14; P295, p. 5","Each new category matches a disclosed event (Dollar Thrifty integration, headquarters move, Simply Wheelz bankruptcy, convertible note conversion, pension withdrawal and Hurricane Sandy), and the prior periods had none","The set of excluded items widened in FY2013, raising the gap between adjusted and GAAP pre-tax income; Integration and Relocation were not defined in the releases that introduced them","E9, E10, E13","Definitions in the introducing releases: not found in P287, P293; given later in the FY2013 10-K (P77, p. 135; P62, pp. 44 and 65)",P3,
F3-C4-01,C4 Prominence: adjusted measures lead,Q1 FY2011 to Q4 FY2013,"First adjusted measure precedes the first GAAP measure in 10 of 12 headline blocks and 12 of 12 opening paragraphs; GAAP present in all 12 headline blocks and opening paragraphs [calc]; titles such as ""Nine Consecutive Quarters of Record Adjusted Pre-Tax Income""","P271 to P295, p. 1 (first 60 words in Table 5c); P293, p. 1","Every release states GAAP pre-tax income and EPS in the bullets and first paragraph with full reconciliations, and the adjusted measure is the company's segment measure",The ordering gives adjusted figures more prominence than GAAP figures; releases furnished under Item 2.02 are subject to the equal-or-greater-prominence requirement [unverified: rule text not in pack],none,Item 10(e)(1)(i)(A) and Form 8-K Item 2.02 instruction text; any SEC comment correspondence: not in pack,P3,
F3-B4-01,B4 GMI rising for three pairs,FY2013 / FY2012,"GMI 0.8190, 0.8484, 0.9559, 0.9942 (1.0001 against FY2012 as revised); cost-line margin 0.1529, 0.1867, 0.2201, 0.2302, 0.2316 [calc]. Triggers (a) and (b)","P1, IS_A and EXTRA (direct operating; depreciation of revenue earning equipment and lease charges)",Margin rose every year; GMI approaches 1 from below as recovery gains level off,"Margin gains have flattened while fleet depreciation-rate reductions (130.1 in FY2012, 39.6 in FY2013) were part of the cost line, so the margin level partly rests on estimate changes","E22, E24 (vendor incentives moved into fleet cost), E9","Cost-line margin excluding rate changes and disposal adjustments: inputs in pack (Note 8), not computed here",P3,
F3-B1-01,B1/B2 Balance-sheet and cash-flow accruals diverge; residuals not traced,FY2010 to FY2013,"Balance-sheet minus cash-flow accrual numerator -180.4, 414.8, 600.0, 726.6 (-0.0108 to 0.0304 of average total assets); FY2013 receivables line differs by 408.7, of which 260.0 lower fleet-sale receivables and 45.9 provision, leaving 102.8 (118.5 after property-sale receivables) not traced; prepaid and other 205.7; accrued liabilities -101.0 [calc]","P1, BS_A, CF_A, EXTRA; P66, pp. 75 and 80 to 81","Acquisitions and de-consolidation (E2, E9, E15, E16), fleet-related non-cash investing balances, restricted cash (investing) and deferred taxes (non-current) sit in the balance-sheet measure and not in operating cash flow; FY2010 payables difference lines up with fleet purchases held in payables","Part of the FY2013 movement in receivables and accrued liabilities is not traced to a disclosed line, so some operating balance changes may sit outside operating cash flow","E2, E9, E10, E15, E16; tie-out W1","Receivables and accrued-liability rollforwards; balances removed with the China entities: not found in P70, P66",P3,
F3-C17-01,C17 Cash from operations and free cash flow relative to income at series low,FY2013,"CFO / income 11.41, 11.18, 10.37; FCF / income 9.97, 9.89, 9.46 (FY2011 to FY2013; FY2009 and FY2010 were losses); FCF after net fleet capex / income 1.78, -0.34, 0.70 [calc]. Trigger (a)","P1, CF_A and IS_A","Ratios near 10 are structural: fleet depreciation is an operating add-back and fleet purchases are investing; income grew faster than cash flow in the highest-income year, with deferred tax up to 241.3","Free cash flow after fleet reinvestment has been below income since FY2012 and was negative in FY2012, so reported income is not matched by cash after fleet replacement",E9; E24 (FY2012 CFO revised -8.3); tie-out W1,Fleet financing flows and program-car repurchase receipts: partly in P295 Table 7,P3,
F3-C7-01,C7 Interest capitalized referenced but not quantified,FY2011 to FY2013,"""Interest (net of amounts capitalized)"" in each cash flow statement and ""net of amounts capitalized"" in MD&A; ""capitalized interest"", ""interest capitalized"" and ""construction in progress"" return 0 hits in 298 files [calc, search]","P66, p. 81; P62, p. 66; P9, p. 90; P37, p. 78",Capitalized interest is nil or immaterial and the caption is standard wording,"If interest is capitalized in amounts that matter, part of interest cost is deferred to the balance sheet without a stated amount",none,Interest incurred and capitalized by year (ASC 835-20 disclosure) [unverified: standard not in pack]; not in pack,P3,
F3-C17-02,C17 Company free cash flow excludes DTG items in FY2012,FY2012 and FY2013,"""(1) 2012 free cash flow excludes certain DTG acquisition related items of approximately $129.6 million as previously disclosed.""; FY2013 free cash flow ""$448.7 million an increase of $293.6 million""","P295, p. 2 and Table 7, line 599","One-off acquisition-related cash items were removed so the years compare on operating terms, and the exclusion is footnoted","The direction of the excluded items is not stated, so the effect on the reported FY2013 increase cannot be read from the release; the company measure also differs from the step 7 measure",E9,"Composition of the 129.6: not found in P295, P296",P4,
F3-B4-02,B4 SGI highest in series,FY2013 / FY2012,SGI 1.1941 against 1.0649 to 1.0973 in earlier pairs [calc]. Trigger (a),"P1, IS_A",Full year of Dollar Thrifty in FY2013 against 43 days in FY2012,Post-acquisition growth is the setting in which the SGI term was estimated as a pressure indicator,"E9, E10, E15","Revenue growth excluding Dollar Thrifty: release attributes U.S. growth ""primarily due to Dollar Thrifty"" (P295, p. 1); amount not found",P4,
F3-B4-03,B4 SGAI lowest in series,FY2013 / FY2012,SGAI 0.9051 (0.8846 against FY2012 as revised); SG&A / revenue 0.1048 (FY2012; 0.1073 revised) to 0.0949 (FY2013) [calc]. Trigger (a): lower SGAI raises M,"P1, IS_A; P66, p. 76",Dollar Thrifty synergies and scale; FY2012 SG&A carried Dollar Thrifty acquisition costs,SG&A fell as a share of revenue in a period when costs were reclassified between SG&A and fleet cost (E24),"E9, E24","SG&A excluding acquisition and integration costs by year: partly in release Table 5 (P285, P295)",P4,
F3-B5-01,B5 F-score above 1.0 on workbook mapping; soft assets rising,FY2011 to FY2013,"F-score 1.768, 1.850 (1.8497), 1.766; soft assets 0.7959, 0.8764, 0.9154, 0.9212 (FY2010 to FY2013), highest in FY2013 and up three years; largest contributions soft assets (+1.82 in FY2013) and issuance (+1.029); fleet in PP&E gives 0.573, 0.620, 0.566 [calc]. Triggers (a) and (b) on soft assets","P1, BS_A and CF_A","The rental fleet (0.55 to 0.58 of assets) is outside the P1 PP&E line, and goodwill and intangibles rose from 0.1672 to 0.2308 of assets with Dollar Thrifty; issuance is 1 for a company that refinances fleet debt continuously","A larger share of assets rests on valuation estimates (goodwill, intangibles, fleet residuals), mostly from acquisitions","E2, E9, E21","Goodwill and trade-name impairment testing (Note 3, in pack; F4)",P4,
F3-B6-01,B6 Cash sales growth highest in series,FY2013,"Change in cash sales 0.0674, 0.0886, 0.2737 against FY2013 revenue growth 0.1941 and receivables growth -0.1982; FY2013 cash-flow accruals -0.1355 and RSST 0.0156 [calc]. Trigger (a)","P1, IS_A, BS_A, EXTRA","Fleet-sale receivables (investing) fell 260.0, Dollar Thrifty contributed a full year and the China entities left the balance sheet; accruals are low, so the step 4 pairing with high accruals does not arise",The part of the receivables decline not traced to a line (F3-B1-01) would lift cash sales without a cash counterpart in operations,"E9, E15","Receivables rollforward (F2, A1 to A8)",P4,
F3-C19-01,C19 Cash-flow classification revisions for fleet lease payments,Q1 2010 to Q3 2010 comparatives,"""we have revised net cash provided by operating activities and net cash used in investing activities ... due to a gross-up of cash lease payments relating to our revenue earning equipment""; parent-only return of capital moved to investing; amounts for the gross-up not stated","P91, p. 7; P131 (Q3 2011 10-Q Note 2); P37, p. 138",Presentation corrections that the company disclosed when made,"Classification of fleet-related cash between operating and investing was corrected more than once, so operating cash flow trends across 2010 may include classification effects","E1, E12, E17 (F1-C15-3)","Amounts of the gross-up: not found in P91, P131",P4,
```

## 7. Looked for and not found

All searches ran in code over the 298 text files listed in the manifest (P2 to P299), case-insensitive, plus the P1 sheets [calc, f3_search.py].

1. Change-in-estimate disclosures near reserves, allowances, provisions or accruals (C6): "change in estimate", "change in accounting estimate", "changes in estimate": 0 hits in 298 files. Reserve text found describes method only (item 25 above).
2. Capitalized software or development amounts (C7): "capitalized software" 0 hits; "software development" 0; "internal use software" 6 hits, all in useful-life tables (P9, P11, P37, P39, P66, P68). No capitalized-software line in P1 BS_A or CF_A.
3. Interest capitalized and construction in progress (C7): "capitalized interest" 0; "interest capitalized" 0; "construction in progress" 0; "amounts capitalized" 27 hits, all inside "net of amounts capitalized" captions. P1 NOTES "Interest incurred" and "Interest capitalized" are blank.
4. Capitalized contract costs (C7): "contract costs", "costs to obtain", "deferred commissions": 0 hits. P1 "Capitalized contract costs" blank.
5. Useful-life search terms (C8): "salvage" 0, "estimated life" 0, "depreciation method" 1 (P294, slide 10, a call-slide reference, not a policy statement); "useful life" 12, "useful lives" 38, "residual value" 268, "holding period" 48 hits, the policy statements quoted in items 22 to 24.
6. Cash-flow classification (C19): "collections on beneficial interests" 0; "deferred purchase price" 0; "interest paid" 0 (statements use "Interest (net of amounts capitalized)"); "taxes on the gain" 0; "classified as operating" 0; "classified as financing" 0. "Securitization" hits are fleet debt facilities; "beneficial interest" hits are one debt facility (item 31). No receivable sale or deferred-purchase-price arrangement found.
7. Explanation of the "Non-cash debt charges" to "Debt-related charges" relabel: P295 and P296 searched for "non-cash debt", "previously", "formerly", "renamed", "conform", "reclassif"; hits concern the E24 revision and the segment change only.
8. Explanation of the Q2 2012 re-categorization in the Q2 FY2013 release: P289 searched for "reclassif", "conform", "integration"; hits are table rows only.
9. Definitions of Integration expenses (P287) and Relocation costs (P293, P294) in the releases that introduced them: searched "integrat" and "relocat"; table rows and a CEO remark only. Definitions found later in the FY2013 10-K (P77, P62).
10. Recast of prior periods for new non-GAAP categories: "recast" in the release files returns 114 word matches, all inside "forecast", "forecasted", "forecasting" or "forecasts" [calc]; prior-year columns show no amount for new categories.
11. The balance-sheet line holding the China Auto Rental investment: P70 and P81 searched for "China Auto Rental" with "prepaid" and "other assets"; not stated.
12. Rule texts: Item 10(e) of Regulation S-K, Form 8-K Item 2.02 instructions and ASC 835-20 are not in the pack; statements about them carry [unverified].

## 8. Could not run

1. B1, B2, B3 for FY2009: no FY2008 balance sheet in P1 [P1, BS_A].
2. B1 trailing-four-quarter windows ending before Q4 FY2011: no 2010 quarters in P1 [P1, IS_Q].
3. B4 pair FY2009 / FY2008: no FY2008 [P1].
4. B5 for FY2009 and FY2010: needs FY2007 and FY2008 year-ends [P1].
5. B6 change in cash sales for FY2010: needs FY2008 receivables [P1].
6. C4 stock-based compensation as a share of GAAP operating income: no operating-income line [P1, IS_Q; P0, Known limits]; run against GAAP pre-tax income and revenue instead.
7. C7 capitalized software or development cost growth against revenue growth: amounts not disclosed (section 7, item 2).
8. C7 capitalized contract costs: none disclosed (section 7, item 4).
9. C7 interest capitalized ÷ interest incurred and construction in progress: amounts not disclosed (section 7, item 3).
10. IFRS-only steps (US-basis cash from operations, IAS 38 capitalization share, revaluation-model note, IAS 8 reserve test): framework is US GAAP [P0].
11. Non-GAAP regimes other than the US (NI 52-112, IFRS 18 note): not applicable; US registrant [P0; context sheet, Basis].

Run on substitute lines, not as specified (stated in the header): B2 (current totals and current portion of long-term debt blank), B3 (investments blank, debt one line), B4 GMI (no cost of sales), AQI and LVGI (no current totals), and B5 soft assets (PP&E mapping shown both ways) [P0, Known limits; P1, BS_A].

## 9. Code

All scripts were run with Python 3 in this order. Inputs: `statements.xlsx` (P1) and the text files; nothing else.

**f3_load.py**

```python
# f3_load.py : load P1 (statements.xlsx) and the FY2012-as-revised column of P66
import openpyxl, re, os
PACK = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\tests\hertz-fy2013\pack"
wb = openpyxl.load_workbook(os.path.join(PACK, "statements.xlsx"), data_only=True)

def sheet(name, key_cols=1):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    out = {}
    for r in rows[1:]:
        if key_cols == 1:
            out[r[0]] = {hdr[i]: r[i] for i in range(1, len(hdr))}
        else:  # EXTRA: key = (statement, label, element)
            out[(r[0], r[1], r[2])] = {hdr[i]: r[i] for i in range(3, len(hdr))}
    return out

IS_A, BS_A, CF_A = sheet("IS_A"), sheet("BS_A"), sheet("CF_A")
IS_Q, BS_Q, CF_Q = sheet("IS_Q"), sheet("BS_Q"), sheet("CF_Q")
EXTRA = sheet("EXTRA", key_cols=3)

def ex(element, label=None):
    """EXTRA row by element name (and label if ambiguous)."""
    hits = [v for k, v in EXTRA.items() if k[2] == element and (label is None or k[1] == label)]
    assert len(hits) == 1, (element, label, len(hits))
    return hits[0]

YEARS = ["FY2009", "FY2010", "FY2011", "FY2012", "FY2013"]
QTRS = [f"Q{q} FY{y}" for y in (2011, 2012, 2013) for q in (1, 2, 3, 4)]

# Annual inputs (USD millions, as originally reported, P1)
A = {}
for y in YEARS:
    A[y] = dict(
        rev=IS_A["Revenue"][y],
        sga=IS_A["Selling, general and administrative"][y],
        dep_pe=IS_A["Depreciation (excluding amortization of intangibles)"][y],
        dep_ree=IS_A["Depreciation of equipment held for rental or lease"][y],
        amort=IS_A["Amortization of intangibles"][y],
        ni=IS_A["Income from continuing operations"][y],
        pretax=IS_A["Pre-tax income"][y],
        dir_op=ex("us-gaap:DirectOperatingCosts")[y],
        dep_ree_lease=ex("htz:CostOfServicesDepreciationAndLeaseCharges")[y],
        cash=BS_A["Cash and equivalents"][y],
        rcash=ex("us-gaap:RestrictedCashAndCashEquivalents")[y],
        rec=BS_A["Trade receivables, net"][y],
        inv=BS_A["Inventory, net"][y],
        prepaid=ex("us-gaap:PrepaidExpenseAndOtherAssets")[y],
        pe_gross=BS_A["PP&E, gross"][y],
        pe_net=BS_A["PP&E, net"][y],
        ree_gross=BS_A["Equipment held for rental or lease, gross"][y],
        ree_net=BS_A["Equipment held for rental or lease, net"][y],
        gw=BS_A["Goodwill"][y],
        intang=BS_A["Intangible assets, net"][y],
        ta=BS_A["Total assets"][y],
        ap=BS_A["Trade payables"][y],
        accr=BS_A["Accrued liabilities"][y],
        tax_pay=BS_A["Income taxes payable"][y],
        debt=ex("us-gaap:DebtAndCapitalLeaseObligations")[y],
        plpd=ex("htz:PublicAndPropertyDamageLiability")[y],
        dtl=(ex("us-gaap:DeferredIncomeTaxLiabilities")[y] or ex("us-gaap:DeferredTaxLiabilities")[y]),
        tl=BS_A["Total liabilities"][y],
        te=BS_A["Total equity"][y],
        cfo=CF_A["Cash from operations"][y],
        da=CF_A["Depreciation and amortization"][y],
        capex_pe=-CF_A["Capital expenditures (PP&E)"][y],
        ree_buy=-CF_A["Purchases of equipment held for rental or lease"][y],
        ree_sell=CF_A["Proceeds from disposal of equipment held for rental or lease"][y],
        pe_sell=CF_A["Proceeds from disposals"][y],
        acq=-CF_A["Acquisitions, net of cash"][y],
        debt_iss=CF_A["Debt issued"][y],
        stock_iss=CF_A["Stock issued"][y],
        sbc=CF_A["Stock-based compensation"][y],
        rcash_chg_cf=ex("us-gaap:IncreaseDecreaseInRestrictedCash")[y],
        dtax_cf=(ex("htz:DeferredIncomeTaxNoncashExpenseBenefit")[y] if ex("htz:DeferredIncomeTaxNoncashExpenseBenefit")[y] is not None
                 else ex("us-gaap:DeferredIncomeTaxExpenseBenefit")[y]),
        ree_rec_noncash=ex("htz:SalesOfRevenueEarningEquipmentEarnedButNotReceived")[y],
        ree_ap_noncash=ex("htz:PurchasesOfRevenueEarningEquipmentIncurredButNotYetPaid")[y],
    )

# Quarterly inputs (P1)
Q = {}
for q in QTRS:
    Q[q] = dict(
        rev=IS_Q["Revenue"][q], ni=IS_Q["Income from continuing operations"][q],
        pretax=IS_Q["Pre-tax income"][q], ta=BS_Q["Total assets"][q],
        cfo=CF_Q["Cash from operations"][q], capex_pe=-CF_Q["Capital expenditures (PP&E)"][q],
        ree_buy=-CF_Q["Purchases of equipment held for rental or lease"][q],
        ree_sell=CF_Q["Proceeds from disposal of equipment held for rental or lease"][q],
        dep_pe=IS_Q["Depreciation (excluding amortization of intangibles)"][q],
        dep_ree=IS_Q["Depreciation of equipment held for rental or lease"][q],
        sbc=CF_Q["Stock-based compensation"][q],
    )

# ---- FY2012 as revised and FY2011 as reprinted, from P66 (FY2013 10-K, USD millions) ----
P66 = open(os.path.join(PACK, "AR-FY2013_financial-statements.txt"), encoding="utf-8").read().splitlines()

def num(s):
    s = s.strip().replace("$", "").replace(",", "")
    if s in ("\u2014", "-", ""):
        return 0.0
    neg = s.startswith("(") and s.endswith(")")
    return -float(s.strip("()")) if neg else float(s)

def p66(label, col, start_marker, occurrence=1):
    """Value in column `col` (0 = first number) of the first row starting with `label`
    after the line containing `start_marker`."""
    i0 = next(i for i, l in enumerate(P66) if start_marker in l)
    n = 0
    for l in P66[i0:]:
        if l.startswith(label + " |"):
            n += 1
            if n == occurrence:
                return num(l.split("|")[1 + col])
    raise KeyError(label)

BSM, ISM, CFM = "CONSOLIDATED BALANCE SHEETS", "CONSOLIDATED STATEMENTS OF OPERATIONS", "CONSOLIDATED STATEMENTS OF CASH FLOWS"
R12 = dict(  # FY2012 as revised (column 1 of the balance sheet, column 1 of IS and CF)
    cash=p66("Cash and cash equivalents", 1, BSM), rcash=p66("Restricted cash and cash equivalents", 1, BSM),
    rec=p66("Receivables, less allowance for doubtful accounts of $30.8 and $29.3", 1, BSM),
    inv=p66("Inventories, at lower of cost or market", 1, BSM), prepaid=p66("Prepaid expenses and other assets", 1, BSM),
    ree_net=p66("Total revenue earning equipment", 1, BSM), pe_net=p66("Total property and equipment", 1, BSM),
    intang=p66("Other intangible assets, net", 1, BSM), gw=p66("Goodwill", 1, BSM), ta=p66("Total assets", 1, BSM),
    ap=p66("Accounts payable", 1, BSM), accr=p66("Accrued liabilities", 1, BSM), tax_pay=p66("Accrued taxes", 1, BSM),
    debt=p66("Debt", 1, BSM), plpd=p66("Public liability and property damage", 1, BSM),
    dtl=p66("Deferred taxes on income", 1, BSM), tl=p66("Total liabilities", 1, BSM),
    rev=p66("Total revenues", 1, ISM), dir_op=p66("Direct operating", 1, ISM),
    dep_ree_lease=p66("Depreciation of revenue earning equipment and lease charges", 1, ISM),
    sga=p66("Selling, general and administrative", 1, ISM), pretax=p66("Income before income taxes", 1, ISM),
    ni=p66("Net income", 1, ISM),
    cfo=p66("Net cash provided by operating activities", 1, CFM),
    dep_ree=p66("Depreciation of revenue earning equipment", 1, CFM), dep_pe=p66("Depreciation of property and equipment", 1, CFM),
    capex_pe=-p66("Property and equipment expenditures", 1, CFM),
    ree_rec_noncash=p66("Sales of revenue earning equipment included in receivables", 1, CFM),
)
R12["pe_gross"] = p66("Land, buildings and leasehold improvements", 1, BSM) + p66("Service equipment and other", 1, BSM)
R12["ree_gross"] = p66("Cars", 1, BSM) + p66("Other equipment", 1, BSM)
R13_ree_rec_noncash = p66("Sales of revenue earning equipment included in receivables", 0, CFM)
R11_ree_rec_noncash = p66("Sales of revenue earning equipment included in receivables", 2, CFM)
R11 = dict(rev=p66("Total revenues", 2, ISM), ni=p66("Net income", 2, ISM), cfo=p66("Net cash provided by operating activities", 2, CFM),
           sga=p66("Selling, general and administrative", 2, ISM), dir_op=p66("Direct operating", 2, ISM),
           dep_ree_lease=p66("Depreciation of revenue earning equipment and lease charges", 2, ISM))

if __name__ == "__main__":
    # Tie-out 1: balance-sheet components sum to totals (checks that the proxy lines are complete)
    for y in YEARS:
        a = A[y]
        assets = a["cash"] + a["rcash"] + a["rec"] + a["inv"] + a["prepaid"] + a["ree_net"] + a["pe_net"] + a["gw"] + a["intang"]
        liabs = a["ap"] + a["accr"] + a["tax_pay"] + a["debt"] + a["plpd"] + a["dtl"]
        print(y, "assets lines - TA =", round(assets - a["ta"], 1), "| liab lines - TL =", round(liabs - a["tl"], 1))
    r = R12
    assets = r["cash"] + r["rcash"] + r["rec"] + r["inv"] + r["prepaid"] + r["ree_net"] + r["pe_net"] + r["gw"] + r["intang"]
    liabs = r["ap"] + r["accr"] + r["tax_pay"] + r["debt"] + r["plpd"] + r["dtl"]
    print("FY2012 revised (P66): assets lines - TA =", round(assets - r["ta"], 1), "| liab lines - TL =", round(liabs - r["tl"], 1))
    print("R12:", R12)
    print("R11:", R11, "R11 ree_rec:", R11_ree_rec_noncash, "R13 ree_rec:", R13_ree_rec_noncash)
```

**f3_compute.py**

```python
# f3_compute.py : F3 steps 1-4, 6 and 7 (numbers), USD millions
import math
from f3_load import A, Q, YEARS, QTRS, R12, R11, R13_ree_rec_noncash

def avg_ta(y):
    i = YEARS.index(y)
    return None if i == 0 else (A[YEARS[i - 1]]["ta"] + A[y]["ta"]) / 2

def ca_proxy(a):   # current-asset lines of the unclassified balance sheet
    return a["cash"] + a["rcash"] + a["rec"] + a["inv"] + a["prepaid"]

def cl_proxy(a):   # non-debt liabilities normally current: payables, accrued liabilities, accrued taxes
    return a["ap"] + a["accr"] + a["tax_pay"]

def wc(a):  return (ca_proxy(a) - a["cash"]) - cl_proxy(a)
def nco(a): return (a["ta"] - ca_proxy(a)) - (a["tl"] - cl_proxy(a) - a["debt"])
def fin(a): return -a["debt"]

def f(x, d=4):
    return "n/a" if x is None else f"{x:.{d}f}"

# -------- STEP 1: accruals --------
print("=== STEP 1: accruals (as originally reported, P1) ===")
S1 = {}
for y in YEARS[1:]:
    a, p = A[y], A[YEARS[YEARS.index(y) - 1]]
    at = avg_ta(y)
    cf_num = a["ni"] - a["cfo"]
    bs_num = ((a["rcash"] + a["rec"] + a["inv"] + a["prepaid"]) - (p["rcash"] + p["rec"] + p["inv"] + p["prepaid"])) \
             - ((a["ap"] + a["accr"]) - (p["ap"] + p["accr"])) - a["da"]
    dwc, dnco, dfin = wc(a) - wc(p), nco(a) - nco(p), fin(a) - fin(p)
    check = (a["te"] - p["te"]) - (a["cash"] - p["cash"])
    S1[y] = dict(avgTA=at, cf_acc=cf_num / at, bs_acc=bs_num / at, cf_num=cf_num, bs_num=bs_num, gap=bs_num - cf_num,
                 dWC=dwc / at, dNCO=dnco / at, dFIN=dfin / at, rsst=(dwc + dnco + dfin) / at, check=(dwc + dnco + dfin) - check,
                 d_rcash=a["rcash"] - p["rcash"], d_rec=a["rec"] - p["rec"], d_ap=a["ap"] - p["ap"],
                 d_ree_rec=a["ree_rec_noncash"] - p["ree_rec_noncash"], d_ree_ap=a["ree_ap_noncash"] - p["ree_ap_noncash"],
                 dtax=a["dtax_cf"], acq=a["acq"], dwc_abs=dwc, dnco_abs=dnco, dfin_abs=dfin)
    s = S1[y]
    print(y, f"avgTA {at:.1f} | NI-CFO {cf_num:.1f} | CF accruals {s['cf_acc']:.4f} | BS(Sloan) num {bs_num:.1f} | BS accruals {s['bs_acc']:.4f} "
          f"| gap BS-CF {s['gap']:.1f} | dWC {s['dWC']:.4f} dNCO {s['dNCO']:.4f} dFIN {s['dFIN']:.4f} RSST {s['rsst']:.4f} (identity check {s['check']:.1f})")
    print("    reconciling lines: d restricted cash", round(s["d_rcash"], 1), "| d fleet-sale receivables (non-cash supplemental)", s["d_ree_rec"] and round(s["d_ree_rec"], 1),
          "| d fleet purchases in payables (supplemental)", s["d_ree_ap"] and round(s["d_ree_ap"], 1), "| deferred tax (CF add-back)", s["dtax"],
          "| acquisitions, net of cash", s["acq"], "| dWC/dNCO/dFIN abs", round(dwc, 1), round(dnco, 1), round(dfin, 1))

# FY2013 on the revised FY2012 base (P66)
a, p = A["FY2013"], R12
at = (p["ta"] + a["ta"]) / 2
cf_num = a["ni"] - a["cfo"]
bs_num = ((a["rcash"] + a["rec"] + a["inv"] + a["prepaid"]) - (p["rcash"] + p["rec"] + p["inv"] + p["prepaid"])) - ((a["ap"] + a["accr"]) - (p["ap"] + p["accr"])) - a["da"]
p_te = p["ta"] - p["tl"]
dwc, dnco, dfin = wc(a) - wc(p), nco(a) - nco(p), fin(a) - fin(p)
S1["FY2013r"] = dict(avgTA=at, cf_acc=cf_num / at, bs_acc=bs_num / at, dWC=dwc / at, dNCO=dnco / at, dFIN=dfin / at, rsst=(dwc + dnco + dfin) / at,
                     gap=bs_num - cf_num, check=(dwc + dnco + dfin) - ((a["te"] - p_te) - (a["cash"] - p["cash"])), dwc_abs=dwc, dnco_abs=dnco, dfin_abs=dfin)
s = S1["FY2013r"]
print("FY2013 on revised FY2012 base:", f"avgTA {at:.1f} CF acc {s['cf_acc']:.4f} BS acc {s['bs_acc']:.4f} gap {s['gap']:.1f} dWC {s['dWC']:.4f} dNCO {s['dNCO']:.4f} dFIN {s['dFIN']:.4f} RSST {s['rsst']:.4f} check {s['check']:.1f}",
      "abs", round(dwc, 1), round(dnco, 1), round(dfin, 1))
# FY2012 revised CF accruals (mixed: FY2011 TA as originally reported)
at12r = (A["FY2011"]["ta"] + R12["ta"]) / 2
print("FY2012 revised CF accruals (NI, CFO, TA revised; FY2011 TA original):", f"{(R12['ni'] - R12['cfo']) / at12r:.4f}")

print("\nTTM cash-flow accruals (quarters from P1; opening TA for TTM Q4 FY2011 is BS_A FY2010)")
TTM = {}
for i in range(3, 12):
    qs = QTRS[i - 3:i + 1]
    ni = sum(Q[q]["ni"] for q in qs); cfo = sum(Q[q]["cfo"] for q in qs)
    open_ta = A["FY2010"]["ta"] if i == 3 else Q[QTRS[i - 4]]["ta"]
    at = (open_ta + Q[QTRS[i]]["ta"]) / 2
    capex = sum(Q[q]["capex_pe"] for q in qs); dep_pe = sum(Q[q]["dep_pe"] for q in qs)
    ree_buy = sum(Q[q]["ree_buy"] for q in qs); ree_sell = sum(Q[q]["ree_sell"] for q in qs); dep_ree = sum(Q[q]["dep_ree"] for q in qs)
    TTM[QTRS[i]] = dict(ni=ni, cfo=cfo, avgTA=at, acc=(ni - cfo) / at, cfo_ni=cfo / ni, fcf_ni=(cfo - capex) / ni,
                        fcf_fleet_ni=(cfo - capex - ree_buy + ree_sell) / ni, capex_dep=capex / dep_pe,
                        ree_buy_dep=ree_buy / dep_ree, ree_net_dep=(ree_buy - ree_sell) / dep_ree,
                        fcf=cfo - capex, fcf_fleet=cfo - capex - ree_buy + ree_sell)
    t = TTM[QTRS[i]]
    print("TTM", QTRS[i], f"NI {ni:.1f} CFO {cfo:.1f} avgTA {at:.1f} accruals {t['acc']:.4f} | CFO/NI {t['cfo_ni']:.2f} FCF/NI {t['fcf_ni']:.2f} "
          f"FCF(after net fleet capex)/NI {t['fcf_fleet_ni']:.2f} | capex/dep (P&E) {t['capex_dep']:.2f} fleet purchases/fleet dep {t['ree_buy_dep']:.2f} net fleet capex/fleet dep {t['ree_net_dep']:.2f}")

# -------- STEP 2: Beneish M-score --------
COEF = dict(DSRI=0.920, GMI=0.528, AQI=0.404, SGI=0.892, DEPI=0.115, SGAI=-0.172, TATA=4.679, LVGI=-0.327)
def mscore(c, p, fleet_in_ppe=True, gmi_one=False, rec_ex_fleet=False, c_rec_adj=None, p_rec_adj=None):
    ppe_c = c["pe_net"] + (c["ree_net"] if fleet_in_ppe else 0)
    ppe_p = p["pe_net"] + (p["ree_net"] if fleet_in_ppe else 0)
    dep_c = c["dep_pe"] + (c["dep_ree"] if fleet_in_ppe else 0)
    dep_p = p["dep_pe"] + (p["dep_ree"] if fleet_in_ppe else 0)
    rec_c = c["rec"] - (c_rec_adj if rec_ex_fleet else 0)
    rec_p = p["rec"] - (p_rec_adj if rec_ex_fleet else 0)
    gm = lambda x: (x["rev"] - (x["dir_op"] + x["dep_ree_lease"])) / x["rev"]
    aq = lambda x, ppe: 1 - (ca_proxy(x) + ppe) / x["ta"]
    lev = lambda x: (x["debt"] + cl_proxy(x)) / x["ta"]
    idx = dict(
        DSRI=(rec_c / c["rev"]) / (rec_p / p["rev"]),
        GMI=1.0 if gmi_one else gm(p) / gm(c),
        AQI=1.0 if aq(p, ppe_p) == 0 else aq(c, ppe_c) / aq(p, ppe_p),
        SGI=c["rev"] / p["rev"],
        DEPI=(dep_p / (dep_p + ppe_p)) / (dep_c / (dep_c + ppe_c)),
        SGAI=(c["sga"] / c["rev"]) / (p["sga"] / p["rev"]),
        LVGI=lev(c) / lev(p),
        TATA=(c["ni"] - c["cfo"]) / c["ta"],
    )
    contrib = {k: COEF[k] * v for k, v in idx.items()}
    m = -4.840 + sum(contrib.values())
    return m, idx, contrib, dict(gm_c=gm(c), gm_p=gm(p), aq_c=aq(c, ppe_c), aq_p=aq(p, ppe_p), lev_c=lev(c), lev_p=lev(p))

print("\n=== STEP 2: Beneish M-score ===")
M = {}
pairs = [(YEARS[i - 1], YEARS[i]) for i in range(1, 5)]
c13r = dict(A["FY2013"])  # FY2013 against FY2012 as revised
p12r = dict(A["FY2012"]); p12r.update({k: v for k, v in R12.items()})
for (py, cy) in pairs + [("FY2012r", "FY2013")]:
    p = p12r if py == "FY2012r" else A[py]
    c = A[cy]
    key = f"{cy} vs {py}"
    base = mscore(c, p)
    s_nofleet = mscore(c, p, fleet_in_ppe=False)
    s_gmi1 = mscore(c, p, gmi_one=True)
    p_adj = R12["ree_rec_noncash"] if py == "FY2012r" else p["ree_rec_noncash"]
    s_rec = mscore(c, p, rec_ex_fleet=True, c_rec_adj=c["ree_rec_noncash"], p_rec_adj=p_adj)
    M[key] = dict(base=base, nofleet=s_nofleet, gmi1=s_gmi1, recx=s_rec)
    m, idx, con, aux = base
    print(key, f"M = {m:.3f} ({'above' if m > -1.78 else 'below'} -1.78)")
    for k in COEF:
        print(f"   {k}: index {idx[k]:.4f} contribution {con[k]:+.4f}")
    print("   aux:", {k: round(v, 4) for k, v in aux.items()})
    print(f"   sensitivity: PP&E and Dep excl. fleet M = {s_nofleet[0]:.3f} (AQI {s_nofleet[1]['AQI']:.4f}, DEPI {s_nofleet[1]['DEPI']:.4f}); "
          f"GMI set to 1 M = {s_gmi1[0]:.3f}; receivables ex fleet-sale receivables M = {s_rec[0]:.3f} (DSRI {s_rec[1]['DSRI']:.4f})")

# -------- STEP 3: Dechow F-score --------
print("\n=== STEP 3: Dechow F-score ===")
FC = dict(RSST=0.790, dREC=2.518, dINV=1.191, SOFT=1.979, dCS=0.171, dEARN=-0.932, ISS=1.029)
def cash_sales(y, base=None):
    i = YEARS.index(y)
    a = base or A[y]
    return a["rev"] - (a["rec"] - A[YEARS[i - 1]]["rec"])

F = {}
def fscore(y, c=None, p=None, avg_c=None, ni_p=None, avg_p=None, cs_c=None, cs_p=None, fleet_in_ppe=True, label=None):
    i = YEARS.index(y)
    c = c or A[y]; p = p or A[YEARS[i - 1]]
    avg_c = avg_c or avg_ta(y)
    rsst = ((wc(c) - wc(p)) + (nco(c) - nco(p)) + (fin(c) - fin(p))) / avg_c
    drec = (c["rec"] - p["rec"]) / avg_c
    dinv = (c["inv"] - p["inv"]) / avg_c
    ppe = c["pe_net"] + (c["ree_net"] if fleet_in_ppe else 0)
    soft = (c["ta"] - c["cash"] - ppe) / c["ta"]
    cs_c = cs_c if cs_c is not None else cash_sales(y)
    cs_p = cs_p if cs_p is not None else cash_sales(YEARS[i - 1])
    dcs = (cs_c - cs_p) / cs_p
    ni_p = ni_p if ni_p is not None else p["ni"]
    avg_p = avg_p or avg_ta(YEARS[i - 1])
    dearn = c["ni"] / avg_c - ni_p / avg_p
    iss = 1 if (c["stock_iss"] > 0 or c["debt_iss"] > 0) else 0
    terms = dict(RSST=rsst, dREC=drec, dINV=dinv, SOFT=soft, dCS=dcs, dEARN=dearn, ISS=iss)
    contrib = {k: FC[k] * v for k, v in terms.items()}
    logit = -7.893 + sum(contrib.values())
    prob = math.exp(logit) / (1 + math.exp(logit))
    return dict(terms=terms, contrib=contrib, logit=logit, prob=prob, F=prob / 0.0037, cs_c=cs_c, cs_p=cs_p)

for y in ["FY2011", "FY2012", "FY2013"]:
    F[y] = fscore(y)
    F[y + " (fleet excl. from PP&E)"] = fscore(y, fleet_in_ppe=False)
# FY2013 on the revised FY2012 base: balance sheet FY2012 revised; FY2012 NI revised; avg TA FY2012 = (FY2011 original + FY2012 revised)/2
cs13r = A["FY2013"]["rev"] - (A["FY2013"]["rec"] - R12["rec"])
cs12r = R12["rev"] - (R12["rec"] - A["FY2011"]["rec"])
F["FY2013r"] = fscore("FY2013", p=p12r, avg_c=(R12["ta"] + A["FY2013"]["ta"]) / 2, ni_p=R12["ni"],
                      avg_p=(A["FY2011"]["ta"] + R12["ta"]) / 2, cs_c=cs13r, cs_p=cs12r)
for k, v in F.items():
    print(k, f"logit {v['logit']:.4f} prob {v['prob']:.5f} F {v['F']:.3f}")
    for t in FC:
        print(f"   {t}: value {v['terms'][t]:.4f} contribution {v['contrib'][t]:+.4f}")

# -------- STEP 4: cash sales and growth gaps --------
print("\n=== STEP 4: cash sales ===")
for y in YEARS[1:]:
    cs = cash_sales(y)
    i = YEARS.index(y)
    prev = cash_sales(YEARS[i - 1]) if i >= 2 else None
    rev_g = A[y]["rev"] / A[YEARS[i - 1]]["rev"] - 1
    rec_g = A[y]["rec"] / A[YEARS[i - 1]]["rec"] - 1
    ex_c = A[y]["rec"] - A[y]["ree_rec_noncash"]; ex_p = A[YEARS[i - 1]]["rec"] - A[YEARS[i - 1]]["ree_rec_noncash"]
    print(y, f"cash sales {cs:.1f}", "| % change", f"{(cs / prev - 1):.4f}" if prev else "n/a (needs FY2008 receivables)",
          f"| revenue growth {rev_g:.4f} | receivables growth {rec_g:.4f} | gap (rec - rev) {rec_g - rev_g:.4f}",
          f"| receivables ex fleet-sale receivables growth {ex_c / ex_p - 1:.4f} gap {ex_c / ex_p - 1 - rev_g:.4f}")
rev_g = A["FY2013"]["rev"] / R12["rev"] - 1; rec_g = A["FY2013"]["rec"] / R12["rec"] - 1
print("FY2013 vs FY2012 revised:", f"cash sales {cs13r:.1f} vs {cs12r:.1f} change {(cs13r / cs12r - 1):.4f} | rev growth {rev_g:.4f} rec growth {rec_g:.4f}",
      f"| rec ex fleet-sale rec growth {(A['FY2013']['rec'] - R13_ree_rec_noncash) / (R12['rec'] - R12['ree_rec_noncash']) - 1:.4f}")

# -------- STEP 6: capitalization and estimates --------
print("\n=== STEP 6: capitalization and depreciation ===")
for y in YEARS:
    a = A[y]; i = YEARS.index(y)
    line = f"{y} capex(P&E)/dep(P&E) {a['capex_pe'] / a['dep_pe']:.3f} | fleet purchases/fleet dep {a['ree_buy'] / a['dep_ree']:.3f} | net fleet capex/fleet dep {(a['ree_buy'] - a['ree_sell']) / a['dep_ree']:.3f}"
    if i > 0:
        p = A[YEARS[i - 1]]
        line += f" | dep(P&E)/avg gross P&E {a['dep_pe'] / ((a['pe_gross'] + p['pe_gross']) / 2):.4f} | fleet dep/avg gross fleet {a['dep_ree'] / ((a['ree_gross'] + p['ree_gross']) / 2):.4f}"
    print(line)
print("FY2013 on revised FY2012 base: fleet dep/avg gross fleet", f"{A['FY2013']['dep_ree'] / ((A['FY2013']['ree_gross'] + R12['ree_gross']) / 2):.4f}",
      "| FY2012 revised fleet dep/avg gross fleet (FY2011 original opening)", f"{R12['dep_ree'] / ((A['FY2011']['ree_gross'] + R12['ree_gross']) / 2):.4f}")

# Note 7/8 inputs copied from P16 (FY2011 10-K p.125), P45 (FY2012 10-K p.113), P74 (FY2013 10-K p.126), USD millions
note = {  # depreciation before disposal adjustment, disposal adjustment, rents, rate-change effect (car + equipment)
    "FY2009": dict(dep=1780.1, adj=72.0, rents=81.7, rate=13.2 + 6.1, src="P16"),
    "FY2010": dict(dep=1747.0, adj=42.9, rents=78.2, rate=19.1 + 3.6, src="P16/P45"),
    "FY2011": dict(dep=1921.8, adj=-112.2, rents=96.1, rate=-13.8 - 4.4, src="P16/P45"),
    "FY2012": dict(dep=2165.2, adj=-96.8, rents=79.8, rate=-130.6 + 0.5, src="P45"),
    "FY2013": dict(dep=2407.8, adj=37.2, rents=80.5, rate=-44.2 + 5.0 - 0.4, src="P74"),
}
rev12 = dict(dep=2145.9, adj=-96.8, rents=79.8)  # FY2012 as reprinted in P74
rev11 = dict(dep=1912.3, adj=-112.2, rents=96.1)  # FY2011 as reprinted in P74
for y in YEARS:
    n = note[y]
    tot = n["dep"] + n["adj"] + n["rents"]
    line = (f"{y} note total {tot:.1f} | disposal adj / dep before adj {n['adj'] / n['dep']:.4f} | rate-change effect {n['rate']:.1f} "
            f"= {n['rate'] / A[y]['pretax']:.4f} of pre-tax income as originally reported ({A[y]['pretax']}) = {n['rate'] / n['dep']:.4f} of dep before adj")
    i = YEARS.index(y)
    if i > 0:
        p = A[YEARS[i - 1]]
        line += f" | dep before disposal adj / avg gross fleet {n['dep'] / ((A[y]['ree_gross'] + p['ree_gross']) / 2):.4f}"
    print(line)
print("check P74 FY2012 reprint total", round(rev12["dep"] + rev12["adj"] + rev12["rents"], 1), "FY2011 reprint total", round(rev11["dep"] + rev11["adj"] + rev11["rents"], 1))
print("FY2013 rate-change effect / pre-tax FY2013:", f"{note['FY2013']['rate'] / A['FY2013']['pretax']:.4f}",
      "| US car rate change -44.2 vs US vehicle disposal net loss 48.2: sum", round(-44.2 + 48.2, 1))
print("FY2012 rate-change effect / FY2012 pre-tax as revised (441.4):", f"{note['FY2012']['rate'] / R12['pretax']:.4f}")

# -------- STEP 7: cash-flow comparisons (annual) --------
print("\n=== STEP 7: cash-flow comparisons, annual ===")
S7 = {}
for y in YEARS:
    a = A[y]
    fcf = a["cfo"] - a["capex_pe"]
    fcf_fleet = fcf - a["ree_buy"] + a["ree_sell"]
    S7[y] = dict(cfo_ni=a["cfo"] / a["ni"], fcf_ni=fcf / a["ni"], fcf_fleet_ni=fcf_fleet / a["ni"], fcf=fcf, fcf_fleet=fcf_fleet)
    print(y, f"NI {a['ni']} CFO {a['cfo']} | CFO/NI {a['cfo'] / a['ni']:.2f} | FCF {fcf:.1f} FCF/NI {fcf / a['ni']:.2f} | FCF after net fleet capex {fcf_fleet:.1f} ratio {fcf_fleet / a['ni']:.2f}",
          "(NI negative: ratio not meaningful)" if a["ni"] < 0 else "")
r = R12
print("FY2012 revised:", f"CFO/NI {r['cfo'] / r['ni']:.2f} FCF/NI {(r['cfo'] - r['capex_pe']) / r['ni']:.2f}")
print("FY2011 reprinted:", f"CFO/NI {R11['cfo'] / R11['ni']:.2f}")
```

**f3_nongaap.py**

```python
# f3_nongaap.py : F3 step 5 from the earnings-release text files (P271 ... P295)
import os, re
from f3_load import PACK, Q, QTRS, num

REL = {  # quarter -> (pack ID, file)
    "Q1 FY2011": ("P271", "ER-Q1-FY2011.txt"), "Q2 FY2011": ("P273", "ER-Q2-FY2011.txt"), "Q3 FY2011": ("P275", "ER-Q3-FY2011.txt"),
    "Q4 FY2011": ("P277", "ER-Q4-FY2011.txt"), "Q1 FY2012": ("P279", "ER-Q1-FY2012.txt"), "Q2 FY2012": ("P281", "ER-Q2-FY2012.txt"),
    "Q3 FY2012": ("P283", "ER-Q3-FY2012.txt"), "Q4 FY2012": ("P285", "ER-Q4-FY2012.txt"), "Q1 FY2013": ("P287", "ER-Q1-FY2013.txt"),
    "Q2 FY2013": ("P289", "ER-Q2-FY2013.txt"), "Q3 FY2013": ("P293", "ER-Q3-FY2013.txt"), "Q4 FY2013": ("P295", "ER-Q4-FY2013.txt"),
}
CANON = [  # (canonical category, regex on the company's label)
    ("Purchase accounting", r"^Purchase accounting"),
    ("Debt charges (non-cash / debt-related)", r"^(Non-cash debt charges|Debt-related charges)"),
    ("Restructuring and related", r"^Restructuring"),
    ("Acquisition related costs", r"^Acquisition related costs"),
    ("Integration expenses", r"^Integration expenses"),
    ("Management transition costs", r"^Management transition costs"),
    ("Premiums paid on debt", r"^Premiums paid on debt"),
    ("Derivative (gains) losses", r"^Derivative"),
    ("Pension adjustment", r"^Pension adjustment"),
    ("Relocation costs", r"^Relocation costs"),
    ("Impairment charges and other", r"^Impairment charges and other"),
    ("Other", r"^Other"),
]

def lines(fn):
    return open(os.path.join(PACK, "releases", fn), encoding="utf-8").read().splitlines()

def vals(line):
    return [v.strip() for v in line.split("|")[1:]]

def income_measurements(L):
    i0 = next(i for i, l in enumerate(L) if l.startswith("INCOME MEASUREMENTS"))
    blk = []
    for l in L[i0:i0 + 40]:
        blk.append(l)
        if l.startswith("Earnings Measures, as adjusted") or (blk and len(blk) > 3 and l.startswith("(EPS based") and any(b.startswith("Earnings Measures, as adjusted") for b in blk[:-1])):
            break
    # reported row (may be split over two lines)
    rep = next(i for i, l in enumerate(blk) if l.startswith("Earnings Measures, as reported"))
    rep_line = blk[rep] if "|" in blk[rep] else blk[rep + 1]
    rv = vals(rep_line)
    adj = {}; labels = {}
    for l in blk:
        for cat, rx in CANON:
            if re.match(rx, l) and "|" in l:
                v = vals(l)
                cur, pri = num(v[0]), (num(v[-1]) if len(v) > 1 else 0.0)
                adj[cat] = (cur, pri); labels[cat] = l.split("|")[0].strip()
    ap = next(l for l in blk if l.startswith("Adjusted pre-tax"))
    apv = vals(ap)
    return dict(gaap_pt=num(rv[0]), gaap_ni=num(rv[1]), gaap_eps=num(rv[2]), gaap_pt_prior=num(rv[3]),
                adj_pt=num(apv[0]), adj_pt_prior=num(apv[2]), adj=adj, labels=labels)

def adjusted_ni(L):
    i0 = next(i for i, l in enumerate(L) if l.startswith("INCOME MEASUREMENTS"))
    for j in range(i0, i0 + 45):
        if L[j].startswith("Earnings Measures, as adjusted"):
            l = L[j] if L[j].count("|") >= 3 else L[j + 1]
            v = vals(l)
            return num(v[1]), num(v[2])

def table_current_total(L, header_regex, row_regex):
    """Current-quarter Total column of the first three-month table after header_regex."""
    i0 = next(i for i, l in enumerate(L) if re.search(header_regex, l))
    for l in L[i0:i0 + 60]:
        if re.match(row_regex, l):
            v = vals(l)
            n = len(v)
            return num(v[3] if n == 4 else v[n // 2 - 1])
    return None

def opening(L):
    i0 = next(i for i, l in enumerate(L) if re.match(r"^HERTZ (REPORTS|SETS)", l))
    text = " ".join(L[i0:i0 + 40])
    m = re.search(r"(Park Ridge, NJ|Naples, FL)", text)
    head, body = text[:m.start()], text[m.start():]
    first_par = body.split("  ")[0]
    words = text.split()
    return head, body, " ".join(words[:60])

def first_pos(s, pats):
    ps = [m.start() for p in pats for m in re.finditer(p, s)]
    return min(ps) if ps else None

OUT = {}
for q in QTRS:
    pid, fn = REL[q]
    L = lines(fn)
    im = income_measurements(L)
    ani, aeps = adjusted_ni(L)
    sbc = table_current_total(L, r"NON-CASH EXPENSES AND CHARGES|Non-cash stock-based employee compensation charges", r"^Non-cash stock-based employee compensation charges")
    ce_line = next(l for l in L if re.match(r"^Corporate EBITDA \|", l))  # first occurrence = three-month table
    cv = vals(ce_line); cebitda = num(cv[3] if len(cv) == 4 else cv[len(cv) // 2 - 1])
    head, body, w60 = opening(L)
    # prominence: in the headline block and in the opening paragraph (to the first 'INCOME MEASUREMENTS' or quote)
    par = body.split("Frissora")[0][:1500]
    OUT[q] = dict(pid=pid, **im, adj_ni=ani, adj_eps=aeps, sbc=sbc, cebitda=cebitda, w60=w60,
                  head_gaap=first_pos(head, [r"GAAP"]), head_adj=first_pos(head, [r"[Aa]djusted", r"Corporate EBITDA"]),
                  par_gaap=first_pos(par, [r"GAAP"]), par_adj=first_pos(par, [r"[Aa]djusted", r"Corporate EBITDA"]))

print("quarter | ID | revenue(P1) | GAAP pre-tax | adj pre-tax | gap | gap/revenue | GAAP NI attrib. | adj NI | gap NI/revenue | SBC added back | SBC/GAAP pre-tax | SBC/revenue | Corporate EBITDA")
for q in QTRS:
    o = OUT[q]; rev = Q[q]["rev"]
    g = o["adj_pt"] - o["gaap_pt"]; gn = o["adj_ni"] - o["gaap_ni"]
    sb = o["sbc"]
    print(q, o["pid"], rev, o["gaap_pt"], o["adj_pt"], round(g, 1), f"{g / rev:.4f}", o["gaap_ni"], o["adj_ni"], f"{gn / rev:.4f}", sb,
          (f"{sb / o['gaap_pt']:.4f}" if o["gaap_pt"] > 0 else "n/m (GAAP pre-tax <= 0)"), f"{sb / rev:.4f}", o["cebitda"])
    # tie: adjustments sum to the gap
    s = sum(v[0] for v in o["adj"].values())
    print("    adjustments sum", round(s, 1), "vs gap", round(g, 1), "| labels:", o["labels"])

# Presence matrix: 2010 quarters from the prior-year columns of the 2011 releases, then 2011-2013 current columns
ORDER = ["Q1 FY2010", "Q2 FY2010", "Q3 FY2010", "Q4 FY2010"] + QTRS
pres = {cat: {} for cat, _ in CANON}
for q in QTRS:
    for cat, _ in CANON:
        cur, pri = OUT[q]["adj"].get(cat, (0.0, 0.0))
        pres[cat][q] = cur != 0
        if q.endswith("FY2011"):
            pres[cat][q.replace("FY2011", "FY2010")] = pri != 0
print("\nEPS: quarter | GAAP diluted EPS | adjusted diluted EPS | gap per share | (Corporate EBITDA - GAAP pre-tax) / revenue")
for q in QTRS:
    o = OUT[q]
    print(q, o["gaap_eps"], o["adj_eps"], round(o["adj_eps"] - o["gaap_eps"], 2), f"{(o['cebitda'] - o['gaap_pt']) / Q[q]['rev']:.4f}")
print("\nAnnual sums of current-quarter adjustments:")
for yr in ("FY2011", "FY2012", "FY2013"):
    qs = [q for q in QTRS if q.endswith(yr)]
    for cat in ("Restructuring and related", "Acquisition related costs", "Integration expenses", "Purchase accounting"):
        print(yr, cat, round(sum(OUT[q]["adj"].get(cat, (0, 0))[0] for q in qs), 1))
print("\nPresence matrix (1 = present):")
print("category | " + " | ".join(ORDER) + " | count last 8 (Q1 FY2012-Q4 FY2013) | first appearance")
for cat, _ in CANON:
    row = [int(pres[cat].get(q, False)) for q in ORDER]
    last8 = sum(row[-8:])
    first = next((ORDER[i] for i, v in enumerate(row) if v), None)
    print(cat, "|", " ".join(map(str, row)), "|", last8, "|", first)

print("\nProminence (character position of first 'GAAP' vs first 'adjusted'/'Corporate EBITDA'; None = absent):")
for q in QTRS:
    o = OUT[q]
    print(q, o["pid"], "headline block: GAAP", o["head_gaap"], "adjusted", o["head_adj"], "| opening paragraph: GAAP", o["par_gaap"], "adjusted", o["par_adj"])
    print("    first 60 words:", o["w60"])

n_head_adj_first = sum(1 for q in QTRS if OUT[q]["head_gaap"] is not None and OUT[q]["head_adj"] is not None and OUT[q]["head_adj"] < OUT[q]["head_gaap"])
n_head_gaap = sum(1 for q in QTRS if OUT[q]["head_gaap"] is not None)
n_par_gaap = sum(1 for q in QTRS if OUT[q]["par_gaap"] is not None)
n_par_adj_first = sum(1 for q in QTRS if OUT[q]["par_adj"] is not None and OUT[q]["par_gaap"] is not None and OUT[q]["par_adj"] < OUT[q]["par_gaap"])
title_gaap = 0  # all-caps titles checked by eye in the w60 output: none contains "GAAP"
print(f"\nReleases: {len(QTRS)} | GAAP in headline block: {n_head_gaap} | adjusted before GAAP in headline block: {n_head_adj_first} | GAAP in opening paragraph: {n_par_gaap} | adjusted before GAAP in opening paragraph: {n_par_adj_first}")
pres16 = {cat: sum(int(pres[cat].get(q, False)) for q in ORDER) for cat, _ in CANON}
print("quarters present of 16:", pres16)
```

**f3_search.py**

```python
# f3_search.py : term searches over every pack text file, with page locators
import os, re, glob
from f3_load import PACK

FILES = sorted(glob.glob(os.path.join(PACK, "*.txt")) + glob.glob(os.path.join(PACK, "releases", "*.txt")) + glob.glob(os.path.join(PACK, "proxy", "*.txt")))
MANIFEST = open(os.path.join(PACK, "manifest.md"), encoding="utf-8").read()
PID = {}
for m in re.finditer(r"^\| (P\d+) \| ([^|]+?) \|", MANIFEST, re.M):
    PID[m.group(2).strip()] = m.group(1)

def pid(path):
    rel = os.path.relpath(path, PACK).replace("\\", "/")
    return PID.get(rel, rel)

TEXT = {p: open(p, encoding="utf-8").read().splitlines() for p in FILES}

def page_of(lines, idx):
    for j in range(idx, -1, -1):
        m = re.match(r"^\[p\. ([^\]]+)\]", lines[j])
        if m:
            return m.group(1)
    return "no marker"

def search(term, files=None, show=0):
    rx = re.compile(re.escape(term), re.I)
    hits = []
    for p in (files or FILES):
        L = TEXT[p]
        for i, l in enumerate(L):
            if rx.search(l):
                hits.append((pid(p), page_of(L, i), i + 1))
    nfiles = len({h[0] for h in hits})
    print(f"'{term}': {len(hits)} lines in {nfiles} files", ("| e.g. " + "; ".join(f"{h[0]} p.{h[1]} (line {h[2]})" for h in hits[:show])) if show else "")
    return hits

print("Files searched:", len(FILES))
print("\n-- Step 6 (capitalization, lives, estimates) --")
for t in ["useful life", "useful lives", "residual value", "salvage", "estimated life", "depreciation method", "holding period",
          "change in estimate", "change in accounting estimate", "changes in estimate", "capitalized software", "internal use software",
          "capitalized interest", "interest capitalized", "amounts capitalized", "construction in progress", "contract costs",
          "costs to obtain", "deferred commissions", "software development"]:
    search(t, show=4)
print("\n-- Step 7 (cash-flow classification) --")
for t in ["collections on beneficial interests", "beneficial interest", "deferred purchase price", "securitization", "interest paid",
          "taxes on the gain", "classified as operating", "classified as financing", "gross-up of cash lease payments"]:
    search(t, show=3)
print("\n-- Step 5 (non-GAAP labels) --")
REL = [p for p in FILES if "releases" in p]
AR = [p for p in FILES if os.path.basename(p).startswith("AR-")]
for t in ["non-recurring", "one-time", "unusual/non-recurring", "reclassified to conform", "recast"]:
    search(t, files=REL, show=3)
    search(t, files=AR, show=3)
print("\n-- Quote locators --")
QUOTES = [
    ("AR-FY2011_notes-02-summary-of-significant-accounting-policies.txt", "Cars | 4 to 26 months"),
    ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Cars | 4 to 28 months"),
    ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Cars | 4 to 36 months"),
    ("AR-FY2011_notes-02-summary-of-significant-accounting-policies.txt", "Capitalized internal use software | 1 to 15 years"),
    ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Capitalized internal use software | 1 to 15 years"),
    ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Capitalized internal use software | 1 to 10 years"),
    ("AR-FY2011_notes-02-summary-of-significant-accounting-policies.txt", "Buildings | 3 to 50 years"),
    ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Buildings | 5 to 50 years"),
    ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Other intangible assets | 3 to 10 years"),
    ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Other intangible assets | 3 to 20 years"),
    ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Holding periods are as follows"),
    ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Revenue earning equipment is stated at cost, net of related discounts. Useful lives are as follows"),
    ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "we make periodic adjustments to depreciation rates"),
    ("AR-FY2013_mdna.txt", "Depreciation rates are adjusted prospectively"),
    ("AR-FY2013_mdna.txt", "deterioration in the used vehicle residual values"),
    ("AR-FY2013_mdna.txt", "relocation of our corporate headquarters to Estero"),
    ("AR-FY2013_mdna.txt", "We anticipate that our expenditures related to the move"),
    ("AR-FY2013_mdna.txt", "net of amounts capitalized"),
    ("AR-FY2013_mdna.txt", "Adjusted pre-tax income is calculated as income before income taxes plus certain"),
    ("AR-FY2013_notes-11-segment-information.txt", "Relocation costs | (7.8)"),
    ("AR-FY2013_notes-11-segment-information.txt", "Represents incremental costs incurred directly supporting"),
    ("AR-FY2013_notes-11-segment-information.txt", "Adjusted pre-tax income is calculated"),
    ("AR-FY2013_notes-14-restructuring.txt", "relocation of our corporate headquarters"),
    ("AR-FY2013_financial-statements.txt", "Interest (net of amounts capitalized) | $651.0"),
    ("AR-FY2013_financial-statements.txt", "Sales of revenue earning equipment included in receivables | 357.3"),
    ("AR-FY2012_financial-statements.txt", "We had presented the cash flows from the return of capital"),
    ("Q1-FY2011_notes-02-basis-of-presentation.txt", "gross-up of cash lease payments"),
    ("releases/ER-Q2-FY2013.txt", "Integration expensess (d) | (0.6)"),
    ("releases/ER-Q2-FY2013.txt", "Other unusual/non-recurring (c) | 6.4"),
    ("releases/ER-Q2-FY2013.txt", "Acquisition related costs | 9.1 | 4.5"),
    ("releases/ER-Q2-FY2012.txt", "Acquisition related costs | 4.5 | 6.1"),
    ("releases/ER-Q4-FY2012.txt", "Also includes $17.5 million of pre-acquisition interest"),
    ("releases/ER-Q4-FY2012.txt", "(g) Primarily represents expenses related to the withdrawal"),
    ("releases/ER-Q4-FY2013.txt", "Debt-related charges | 13.8"),
    ("releases/ER-Q4-FY2013.txt", "(d) Represents debt-related charges"),
    ("releases/ER-Q4-FY2013.txt", "2012 free cash flow excludes certain DTG"),
    ("releases/ER-Q4-FY2013.txt", "We had a change in policy in Q1 2013"),
    ("releases/ER-Q4-FY2013.txt", "Corporate EBITDA excludes the impact of extraordinary"),
    ("releases/ER-Q4-FY2013.txt", "Earnings Measures, as reported (EPS based on 464.3M"),
    ("releases/ER-Q1-FY2013.txt", "Assumed provision for income taxes at 35% in 2013"),
    ("releases/ER-Q4-FY2012.txt", "normalized income tax rate (34% in 2012 and 2011)"),
    ("releases/ER-Q3-FY2013.txt", "Note: Certain adjustments have been reclassified"),
    ("releases/ER-Q3-FY2013.txt", "(a) Related to Franchise Services of North America"),
    ("releases/ER-Q3-FY2013.txt", "(b) Primarily represents expenses related to the loss on conversion"),
    ("releases/ER-Q1-FY2011.txt", "certain one-time charges and non-operational items"),
    ("AR-FY2013_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "The loss on vehicle sales"),
    ("AR-FY2013_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "The cumulative effect of the reduction in rates"),
    ("AR-FY2012_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "The cumulative effect of the reduction in rates"),
    ("AR-FY2011_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "These depreciation rate changes resulted"),
    ("AR-FY2013_notes-04-business-combinations-and-divestitures.txt", "Reclassifying non-recurring compensation costs"),
]
for fn, q in QUOTES:
    p = os.path.join(PACK, *fn.split("/"))
    L = TEXT[p]
    idx = next((i for i, l in enumerate(L) if q in l), None)
    print(pid(p), fn, "| p.", page_of(L, idx) if idx is not None else "NOT FOUND", "| line", None if idx is None else idx + 1, "|", q[:70])
```

**f3_extra.py**

```python
# f3_extra.py : soft-asset series, balance-sheet vs cash-flow line reconciliation, ledger trigger checks
from f3_load import A, YEARS, ex, R12
import f3_compute as C   # re-runs step 1-7 printouts; results reused below

print("\n=== soft assets (TA - cash - PP&E net) / TA ===")
for y in YEARS:
    a = A[y]
    lit = (a["ta"] - a["cash"] - a["pe_net"]) / a["ta"]
    flt = (a["ta"] - a["cash"] - a["pe_net"] - a["ree_net"]) / a["ta"]
    print(y, f"workbook mapping (fleet not in PP&E) {lit:.4f} | fleet in PP&E {flt:.4f}")

print("\n=== balance-sheet change vs cash-flow operating line (positive = source of cash / accrual-reducing) ===")
cf_inv_prep = ex("htz:IncreaseDecreaseInInventoriesPrepaidExpenseAndOtherAssets")
cf_tax = ex("us-gaap:IncreaseDecreaseInAccruedIncomeTaxesPayable")
from f3_load import CF_A
for y in YEARS[1:]:
    a, p = A[y], A[YEARS[YEARS.index(y) - 1]]
    rows = [
        ("receivables", -(a["rec"] - p["rec"]), CF_A["Change in receivables"][y]),
        ("inventories + prepaid and other", -((a["inv"] + a["prepaid"]) - (p["inv"] + p["prepaid"])), cf_inv_prep[y]),
        ("accounts payable", a["ap"] - p["ap"], CF_A["Change in payables"][y]),
        ("accrued liabilities", a["accr"] - p["accr"], CF_A["Change in accrued liabilities"][y]),
        ("accrued taxes", a["tax_pay"] - p["tax_pay"], cf_tax[y]),
    ]
    for name, bs, cf in rows:
        print(y, f"{name}: BS-implied {bs:.1f} | CF line {cf} | difference {bs - cf:.1f}")
# FY2013 on the revised FY2012 base
a, p = A["FY2013"], R12
for name, bs, cf in [("receivables", -(a["rec"] - p["rec"]), CF_A["Change in receivables"]["FY2013"]),
                     ("inventories + prepaid and other", -((a["inv"] + a["prepaid"]) - (p["inv"] + p["prepaid"])), cf_inv_prep["FY2013"]),
                     ("accounts payable", a["ap"] - p["ap"], CF_A["Change in payables"]["FY2013"]),
                     ("accrued liabilities", a["accr"] - p["accr"], CF_A["Change in accrued liabilities"]["FY2013"])]:
    print("FY2013 vs FY2012 revised", f"{name}: BS-implied {bs:.1f} | CF line {cf} | difference {bs - cf:.1f}")
print("FY2013 receivables ex fleet-sale receivables: FY2012 revised", round(R12["rec"] - R12["ree_rec_noncash"], 1), "FY2013", round(A["FY2013"]["rec"] - A["FY2013"]["ree_rec_noncash"], 1),
      "change", round((A["FY2013"]["rec"] - A["FY2013"]["ree_rec_noncash"]) - (R12["rec"] - R12["ree_rec_noncash"]), 1))

print("\n=== ledger triggers: (a) latest most adverse, (b) adverse direction >= 3 consecutive YoY comparisons ===")
def trig(name, series, adverse="up"):
    ks = list(series); v = [series[k] for k in ks]
    sgn = 1 if adverse == "up" else -1
    a_hit = all(sgn * v[-1] >= sgn * x for x in v[:-1])
    run = 0
    for i in range(len(v) - 1, 0, -1):
        if sgn * (v[i] - v[i - 1]) > 0:
            run += 1
        else:
            break
    print(f"{name}: {dict(zip(ks, [round(x, 4) for x in v]))} | (a) {a_hit} | (b) run {run} -> {run >= 3}")

trig("CF accruals", {y: C.S1[y]["cf_acc"] for y in YEARS[1:]})
trig("BS accruals", {y: C.S1[y]["bs_acc"] for y in YEARS[1:]})
trig("RSST accruals", {y: C.S1[y]["rsst"] for y in YEARS[1:]})
trig("TTM CF accruals", {q: C.TTM[q]["acc"] for q in C.TTM})
keys = ["FY2010 vs FY2009", "FY2011 vs FY2010", "FY2012 vs FY2011", "FY2013 vs FY2012"]
for mode in ("nofleet", "base"):
    trig(f"M-score ({mode})", {k: C.M[k][mode][0] for k in keys})
    for ix, adv in [("DSRI", "up"), ("GMI", "up"), ("AQI", "up"), ("SGI", "up"), ("DEPI", "up"), ("SGAI", "down"), ("LVGI", "down"), ("TATA", "up")]:
        trig(f"  {ix} ({mode})", {k: C.M[k][mode][1][ix] for k in keys}, adv)
for y in ("FY2011", "FY2012", "FY2013"):
    pass
trig("F-score (fleet in PP&E)", {y: C.F[y]["F"] for y in ("FY2011", "FY2012", "FY2013")})
trig("F-score (workbook mapping)", {y: C.F[y + " (fleet excl. from PP&E)"]["F"] for y in ("FY2011", "FY2012", "FY2013")})
trig("soft assets (workbook mapping)", {y: (A[y]["ta"] - A[y]["cash"] - A[y]["pe_net"]) / A[y]["ta"] for y in YEARS})
trig("soft assets (fleet in PP&E)", {y: (A[y]["ta"] - A[y]["cash"] - A[y]["pe_net"] - A[y]["ree_net"]) / A[y]["ta"] for y in YEARS})
trig("capex/dep P&E", {y: A[y]["capex_pe"] / A[y]["dep_pe"] for y in YEARS})
trig("net fleet capex/fleet dep", {y: (A[y]["ree_buy"] - A[y]["ree_sell"]) / A[y]["dep_ree"] for y in YEARS})
trig("fleet dep / avg gross fleet", {y: A[y]["dep_ree"] / ((A[y]["ree_gross"] + A[YEARS[YEARS.index(y) - 1]]["ree_gross"]) / 2) for y in YEARS[1:]}, "down")
trig("P&E dep / avg gross P&E", {y: A[y]["dep_pe"] / ((A[y]["pe_gross"] + A[YEARS[YEARS.index(y) - 1]]["pe_gross"]) / 2) for y in YEARS[1:]}, "down")
trig("CFO/NI (positive-NI years)", {y: C.S7[y]["cfo_ni"] for y in ("FY2011", "FY2012", "FY2013")}, "down")
trig("FCF/NI (positive-NI years)", {y: C.S7[y]["fcf_ni"] for y in ("FY2011", "FY2012", "FY2013")}, "down")
trig("FCF after net fleet capex / NI", {y: C.S7[y]["fcf_fleet_ni"] for y in ("FY2011", "FY2012", "FY2013")}, "down")
trig("TTM CFO/NI", {q: C.TTM[q]["cfo_ni"] for q in C.TTM}, "down")
trig("TTM FCF/NI", {q: C.TTM[q]["fcf_ni"] for q in C.TTM}, "down")
cs = {y: C.cash_sales(y) for y in YEARS[1:]}
trig("cash sales % change", {y: cs[y] / cs[YEARS[YEARS.index(y) - 1]] - 1 for y in ("FY2011", "FY2012", "FY2013")})
print("F-score FY2012 workbook mapping, 6 dp:", round(C.F["FY2012 (fleet excl. from PP&E)"]["F"], 6))

print("\n=== figures cited in the text ===")
for y in YEARS:
    print(y, f"SG&A/revenue {A[y]['sga'] / A[y]['rev']:.4f}", f"| cost-line gross margin proxy {(A[y]['rev'] - A[y]['dir_op'] - A[y]['dep_ree_lease']) / A[y]['rev']:.4f}")
print("FY2012 revised SG&A/revenue", f"{R12['sga'] / R12['rev']:.4f}")
a, p = A["FY2013"], A["FY2012"]
rec_diff = -(a["rec"] - p["rec"]) - CF_A["Change in receivables"]["FY2013"]
fleet_rec = p["ree_rec_noncash"] - a["ree_rec_noncash"]
prov = ex("us-gaap:ProvisionForDoubtfulAccounts")["FY2013"]
pe_rec = ex("htz:SalesOfPropertyAndEquipmentEarnedButNotReceived")
print("FY2013 receivables line difference", round(rec_diff, 1), "| less decline in fleet-sale receivables", round(fleet_rec, 1), "| less CF provision", prov,
      "| residual", round(rec_diff - fleet_rec - prov, 1), "| P&E-sale receivables FY2012, FY2013:", pe_rec["FY2012"], pe_rec["FY2013"],
      "| residual after P&E-sale receivables increase", round(rec_diff - fleet_rec - prov + (pe_rec["FY2013"] - pe_rec["FY2012"]), 1))
for y in ("FY2010", "FY2011", "FY2012", "FY2013"):
    print(y, "BS-CF accrual gap / avg TA", f"{C.S1[y]['gap'] / C.S1[y]['avgTA']:.4f}")
print("restructuring (sum of quarterly releases) FY2013 vs FY2012 change", f"{100.2 / 49.1 - 1:.4f}")
print("fleet dep/avg gross fleet FY2010 -> FY2013 change (pp)", f"{(C.A['FY2013']['dep_ree'] / ((A['FY2013']['ree_gross'] + A['FY2012']['ree_gross']) / 2) - A['FY2010']['dep_ree'] / ((A['FY2010']['ree_gross'] + A['FY2009']['ree_gross']) / 2)) * 100:.2f}")
ex12 = A["FY2012"]["rec"] - A["FY2012"]["ree_rec_noncash"]; ex11 = A["FY2011"]["rec"] - A["FY2011"]["ree_rec_noncash"]
print("FY2012 receivables ex fleet-sale growth", f"{ex12 / ex11 - 1:.4f}", "revenue growth", f"{A['FY2012']['rev'] / A['FY2011']['rev'] - 1:.4f}")
print("Q4 FY2012 adjusted pre-tax as first released 213.5 vs as reprinted in Q4 FY2013 release 210.7: difference", round(213.5 - 210.7, 1),
      "| GAAP pre-tax -40.3 vs -43.1:", round(-40.3 - -43.1, 1))
print("Q2 FY2013 release: 'Acquisition related costs' + 'Integration expenses' in Table 1 =", round(9.1 + 9.2, 1), "; Corporate EBITDA table =", round(17.6 + 7.7, 1))
print("Q1 FY2012 acquisition related costs 6.9 + Q2 FY2012 4.5 =", round(6.9 + 4.5, 1), "(P289 Table 5 six-month 2012 acquisition related costs: 11.4)")
print("Q1 FY2013 integration 10.8 + Q2 FY2013 9.2 =", round(10.8 + 9.2, 1), "(P289 Table 5 six-month 2013: 20.0)")
print("Relocation: FY2013 7.8 (P295) - Q3 3.9 - Q4 3.4 =", round(7.8 - 3.9 - 3.4, 1), "| nine months 4.4 (P293) - Q3 3.9 =", round(4.4 - 3.9, 1))
print("Restructuring adjustments FY2011, FY2012, FY2013 (sums of quarterly releases): 66.3, 49.1, 100.2; FY2013 release full-year figure 98.8; difference", round(100.2 - 98.8, 1))
print("\nSoft-asset composition (share of total assets):")
for y in YEARS:
    a = A[y]
    print(y, f"fleet {a['ree_net'] / a['ta']:.4f} | goodwill + intangibles {(a['gw'] + a['intang']) / a['ta']:.4f} | restricted cash + receivables + inventory + prepaid {(a['rcash'] + a['rec'] + a['inv'] + a['prepaid']) / a['ta']:.4f}")
```

**f3_fleetq.py**

```python
# f3_fleetq.py : 2013 quarterly path of car-rental depreciation-rate changes and vehicle disposal results
# Inputs copied from the depreciation notes (USD millions; negative rate change = lower depreciation;
# disposal result: positive = net gain, negative = net loss)
#   P213 (Q1 2013 10-Q, p.13): car rental rate change Q1 -0.7; car rental disposal Q1 -3.3
#   P234 (Q2 2013 10-Q, pp.13-14): car rental rate change Q2 -14.8, H1 -15.5; car rental disposal Q2 -17.5, H1 -20.8
#   P254 (Q3 2013 10-Q, pp.13-14): U.S. rate change Q3 -18.0, 9M -35.3; international +2.1 / +3.9;
#        U.S. disposal Q3 -11.1, 9M -20.5; international disposal Q3 -4.3, 9M -15.7
#   P74 (FY2013 10-K, p.126): U.S. rate change FY -44.2; international +5.0; U.S. disposal FY -48.2; international -15.2
q_car_rate = {"Q1": -0.7, "Q2": -14.8}
us_rate_9m, us_rate_q3, us_rate_fy = -35.3, -18.0, -44.2
us_disp_9m, us_disp_q3, us_disp_fy = -20.5, -11.1, -48.2
intl_rate_9m, intl_rate_fy = 3.9, 5.0
intl_disp_9m, intl_disp_fy = -15.7, -15.2
car_disp_h1 = -20.8

us_rate_h1 = us_rate_9m - us_rate_q3
us_rate_q4 = us_rate_fy - us_rate_9m
us_disp_h1 = us_disp_9m - us_disp_q3
us_disp_q4 = us_disp_fy - us_disp_9m
intl_rate_q4 = intl_rate_fy - intl_rate_9m
intl_disp_q4 = intl_disp_fy - intl_disp_9m
print(f"U.S. car rental rate change: H1 {us_rate_h1:.1f} (derived 9M - Q3), Q3 {us_rate_q3}, Q4 {us_rate_q4:.1f} (derived FY - 9M)")
print(f"U.S. car rental vehicle disposal result: H1 {us_disp_h1:.1f}, Q3 {us_disp_q3}, Q4 {us_disp_q4:.1f}")
print(f"Car rental (U.S. + international) H1 disposal result {car_disp_h1} vs Q1 {-3.3} + Q2 {-17.5} = {-3.3 - 17.5:.1f}")
print(f"International: rate change Q4 {intl_rate_q4:.1f}; disposal result Q4 {intl_disp_q4:.1f} (FY loss smaller than 9M loss)")
print(f"U.S. FY2013: rate change {us_rate_fy} alongside disposal net loss {-us_disp_fy}; ratio of Q4 disposal loss to Q4 rate reduction {us_disp_q4 / us_rate_q4:.2f}")
```

**f3_tables.py**

```python
# f3_tables.py : print the computation tables as markdown from the computed objects
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import f3_compute as C
    import f3_nongaap as N
from f3_load import A, YEARS, R12, Q, QTRS

def r(x, d=4):
    return f"{x:.{d}f}"

def table(title, cols, rows):
    print(f"\n{title}\n")
    print("| Line | " + " | ".join(cols) + " | Mark |")
    print("|---|" + "---|" * len(cols) + "---|")
    for name, vals, mark in rows:
        print(f"| {name} | " + " | ".join(vals) + f" | {mark} |")

# Accruals
cols = ["FY2010", "FY2011", "FY2012", "FY2013", "FY2013 (FY2012 as revised)"]
ks = ["FY2010", "FY2011", "FY2012", "FY2013", "FY2013r"]
S = C.S1
table("Table 1a. Accruals and decomposition (USD millions; ratios as decimals of average total assets)", cols, [
    ("Average total assets", [r(S[k]["avgTA"], 1) for k in ks], "[calc]"),
    ("Cash-flow accruals (NI - CFO) / avg TA", [r(S[k]["cf_acc"]) for k in ks], "[calc]"),
    ("Balance-sheet accruals (Sloan, proxy lines) / avg TA", [r(S[k]["bs_acc"]) for k in ks], "[calc]"),
    ("Gap: balance-sheet numerator minus cash-flow numerator", [r(S[k]["gap"], 1) for k in ks], "[calc]"),
    ("dWC / avg TA", [r(S[k]["dWC"]) for k in ks], "[calc]"),
    ("dNCO / avg TA", [r(S[k]["dNCO"]) for k in ks], "[calc]"),
    ("dFIN / avg TA", [r(S[k]["dFIN"]) for k in ks], "[calc]"),
    ("RSST accruals (dWC + dNCO + dFIN) / avg TA", [r(S[k]["rsst"]) for k in ks], "[calc]"),
    ("dWC, dNCO, dFIN (USD m)", [f"{S[k]['dwc_abs']:.1f}; {S[k]['dnco_abs']:.1f}; {S[k]['dfin_abs']:.1f}" for k in ks], "[calc]"),
    ("Identity check: dWC+dNCO+dFIN minus (d equity - d cash)", [r(S[k]["check"], 1) for k in ks], "[calc]"),
])
tk = list(C.TTM)
table("Table 1b. Trailing-four-quarter cash-flow accruals (quarters as originally reported, P1)", tk, [
    ("TTM income from continuing operations", [r(C.TTM[k]["ni"], 1) for k in tk], "[calc]"),
    ("TTM cash from operations", [r(C.TTM[k]["cfo"], 1) for k in tk], "[calc]"),
    ("Average total assets (opening = 4 quarters earlier)", [r(C.TTM[k]["avgTA"], 1) for k in tk], "[calc]"),
    ("Cash-flow accruals", [r(C.TTM[k]["acc"]) for k in tk], "[calc]"),
])

# M-score
pk = ["FY2010 vs FY2009", "FY2011 vs FY2010", "FY2012 vs FY2011", "FY2013 vs FY2012", "FY2013 vs FY2012r"]
pc = ["FY2010 / FY2009", "FY2011 / FY2010", "FY2012 / FY2011", "FY2013 / FY2012", "FY2013 / FY2012 as revised"]
rows = []
for ix in ["DSRI", "GMI", "AQI", "SGI", "DEPI", "SGAI", "LVGI", "TATA"]:
    rows.append((f"{ix} index", [r(C.M[k]["nofleet"][1][ix]) for k in pk], "[calc]"))
    rows.append((f"{ix} contribution ({C.COEF[ix]:+.3f} x index)", [f"{C.M[k]['nofleet'][2][ix]:+.4f}" for k in pk], "[calc]"))
rows.append(("Constant", ["-4.8400"] * 5, "[formula]"))
rows.append(("M-score (workbook mapping)", [r(C.M[k]["nofleet"][0], 3) for k in pk], "[calc]"))
rows.append(("Above -1.78?", ["yes" if C.M[k]["nofleet"][0] > -1.78 else "no" for k in pk], "[calc]"))
rows.append(("Alt. A: fleet in PP&E and Dep: AQI; DEPI; M", [f"{C.M[k]['base'][1]['AQI']:.4f}; {C.M[k]['base'][1]['DEPI']:.4f}; {C.M[k]['base'][0]:.3f}" for k in pk], "[calc]"))
rows.append(("Alt. B: GMI set to 1 (workbook mapping otherwise): M", [r(C.mscore(*( (A[k.split(' vs ')[0]], (C.p12r if k.endswith('r') else A[k.split(' vs ')[1]])) ), fleet_in_ppe=False, gmi_one=True)[0], 3) for k in pk], "[calc]"))
rows.append(("Alt. C: receivables less fleet-sale receivables: DSRI; M (fleet in PP&E)", [f"{C.M[k]['recx'][1]['DSRI']:.4f}; {C.M[k]['recx'][0]:.3f}" for k in pk], "[calc]"))
rows.append(("Cost-line gross margin t-1; t", [f"{C.M[k]['base'][3]['gm_p']:.4f}; {C.M[k]['base'][3]['gm_c']:.4f}" for k in pk], "[calc]"))
table("Table 2. Beneish M-score (workbook mapping: PP&E, net and Dep exclude the rental fleet)", pc, rows)

# F-score (primary = workbook mapping: PP&E, net excludes the rental fleet; alternative = fleet in PP&E)
FW = {k: C.F[k + " (fleet excl. from PP&E)"] for k in ("FY2011", "FY2012", "FY2013")}
FW["FY2013r"] = C.fscore("FY2013", p=C.p12r, avg_c=(R12["ta"] + A["FY2013"]["ta"]) / 2, ni_p=R12["ni"],
                         avg_p=(A["FY2011"]["ta"] + R12["ta"]) / 2, cs_c=C.cs13r, cs_p=C.cs12r, fleet_in_ppe=False)
fk = ["FY2011", "FY2012", "FY2013", "FY2013r"]
fc = ["FY2011", "FY2012", "FY2013", "FY2013 (FY2012 as revised)"]
rows = []
for t in ["RSST", "dREC", "dINV", "SOFT", "dCS", "dEARN", "ISS"]:
    rows.append((f"{t} value", [r(FW[k]["terms"][t]) for k in fk], "[calc]"))
    rows.append((f"{t} contribution ({C.FC[t]:+.3f} x value)", [f"{FW[k]['contrib'][t]:+.4f}" for k in fk], "[calc]"))
rows.append(("Constant", ["-7.8930"] * 4, "[formula]"))
rows.append(("Logit", [r(FW[k]["logit"]) for k in fk], "[calc]"))
rows.append(("Probability", [r(FW[k]["prob"], 5) for k in fk], "[calc]"))
rows.append(("F-score (workbook mapping)", [r(FW[k]["F"], 3) for k in fk], "[calc]"))
rows.append(("Above 1.0 / 1.85 / 2.45?", [("yes" if FW[k]["F"] > 1 else "no") + " / " + ("yes" if FW[k]["F"] > 1.85 else "no") + " / " + ("yes" if FW[k]["F"] > 2.45 else "no") for k in fk], "[calc]"))
rows.append(("Alt. A: fleet in PP&E: SOFT; contribution; F", [f"{C.F[k]['terms']['SOFT']:.4f}; {C.F[k]['contrib']['SOFT']:+.4f}; {C.F[k]['F']:.3f}" for k in fk], "[calc]"))
table("Table 3. Dechow F-score (workbook mapping: PP&E, net excludes the rental fleet)", fc, rows)

# Cash-flow comparisons
yk = YEARS
table("Table 7a. Cash-flow comparisons, annual (USD millions)", yk, [
    ("Income from continuing operations", [r(A[y]["ni"], 1) for y in yk], "[P1, IS_A]"),
    ("Cash from operations", [r(A[y]["cfo"], 1) for y in yk], "[P1, CF_A]"),
    ("CFO / income", [r(C.S7[y]["cfo_ni"], 2) + (" (n/m, loss)" if A[y]["ni"] < 0 else "") for y in yk], "[calc]"),
    ("FCF = CFO - capex (P&E)", [r(C.S7[y]["fcf"], 1) for y in yk], "[calc]"),
    ("FCF / income", [r(C.S7[y]["fcf_ni"], 2) + (" (n/m)" if A[y]["ni"] < 0 else "") for y in yk], "[calc]"),
    ("FCF after net fleet capex = FCF - fleet purchases + fleet disposal proceeds", [r(C.S7[y]["fcf_fleet"], 1) for y in yk], "[calc]"),
    ("FCF after net fleet capex / income", [r(C.S7[y]["fcf_fleet_ni"], 2) + (" (n/m)" if A[y]["ni"] < 0 else "") for y in yk], "[calc]"),
    ("Capex (P&E) / depreciation (P&E)", [r(A[y]["capex_pe"] / A[y]["dep_pe"], 3) for y in yk], "[calc]"),
    ("Fleet purchases / fleet depreciation", [r(A[y]["ree_buy"] / A[y]["dep_ree"], 3) for y in yk], "[calc]"),
    ("Net fleet capex / fleet depreciation", [r((A[y]["ree_buy"] - A[y]["ree_sell"]) / A[y]["dep_ree"], 3) for y in yk], "[calc]"),
])
table("Table 7b. Cash-flow comparisons, trailing four quarters", tk, [
    ("CFO / income", [r(C.TTM[k]["cfo_ni"], 2) for k in tk], "[calc]"),
    ("FCF / income", [r(C.TTM[k]["fcf_ni"], 2) for k in tk], "[calc]"),
    ("FCF after net fleet capex / income", [r(C.TTM[k]["fcf_fleet_ni"], 2) for k in tk], "[calc]"),
    ("Capex (P&E) / depreciation (P&E)", [r(C.TTM[k]["capex_dep"], 2) for k in tk], "[calc]"),
    ("Fleet purchases / fleet depreciation", [r(C.TTM[k]["ree_buy_dep"], 2) for k in tk], "[calc]"),
    ("Net fleet capex / fleet depreciation", [r(C.TTM[k]["ree_net_dep"], 2) for k in tk], "[calc]"),
])

# Non-GAAP gap
table("Table 5a. Adjusted-measure gap by quarter (USD millions; shares of revenue as decimals)", QTRS, [
    ("Revenue (P1)", [r(Q[q]["rev"], 1) for q in QTRS], "[P1, IS_Q]"),
    ("GAAP pre-tax income (release)", [r(N.OUT[q]["gaap_pt"], 1) for q in QTRS], "[release]"),
    ("Adjusted pre-tax income (release)", [r(N.OUT[q]["adj_pt"], 1) for q in QTRS], "[release]"),
    ("Pre-tax gap / revenue", [r((N.OUT[q]["adj_pt"] - N.OUT[q]["gaap_pt"]) / Q[q]["rev"]) for q in QTRS], "[calc]"),
    ("GAAP net income attributable (release)", [r(N.OUT[q]["gaap_ni"], 1) for q in QTRS], "[release]"),
    ("Adjusted net income (release)", [r(N.OUT[q]["adj_ni"], 1) for q in QTRS], "[release]"),
    ("Net income gap / revenue", [r((N.OUT[q]["adj_ni"] - N.OUT[q]["gaap_ni"]) / Q[q]["rev"]) for q in QTRS], "[calc]"),
    ("GAAP diluted EPS; adjusted diluted EPS", [f"{N.OUT[q]['gaap_eps']:.2f}; {N.OUT[q]['adj_eps']:.2f}" for q in QTRS], "[release]"),
    ("Corporate EBITDA (release)", [r(N.OUT[q]["cebitda"], 1) for q in QTRS], "[release]"),
    ("(Corporate EBITDA - GAAP pre-tax) / revenue", [r((N.OUT[q]["cebitda"] - N.OUT[q]["gaap_pt"]) / Q[q]["rev"]) for q in QTRS], "[calc]"),
    ("Stock-based compensation added back (Corporate EBITDA table)", [r(N.OUT[q]["sbc"], 1) for q in QTRS], "[release]"),
    ("SBC / GAAP pre-tax income", [r(N.OUT[q]["sbc"] / N.OUT[q]["gaap_pt"]) if N.OUT[q]["gaap_pt"] > 0 else "n/m" for q in QTRS], "[calc]"),
    ("SBC / revenue", [r(N.OUT[q]["sbc"] / Q[q]["rev"]) for q in QTRS], "[calc]"),
])
```

**f3_ledger.py**

```python
# f3_ledger.py : write the ledger rows as a markdown table and as CSV (formatting only; every figure comes from sections 4 and 5)
import csv, io
COLS = ["ID", "Item", "Period", "Evidence", "Locator", "Benign reading", "Adverse reading", "Context", "Resolving disclosure", "Priority", "Verdict"]
R = []
def row(*v):
    R.append(dict(zip(COLS, list(v) + [""])))

row("F3-C8-01", "C8 Fleet depreciation rates and residual values, stated inconsistency", "FY2013",
    "Note 8: U.S. rate changes \"resulted in net decreases of $44.2 million\" in 2013 and \"The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. for the years ended December 31, 2013, 2012 and 2011.\" Same note: U.S. vehicle disposals had \"net losses of $48.2 million\" in 2013, due to \"declining residual values from falling demand for used vehicles\"; MD&A cites \"a deterioration in the used vehicle residual values\". 2013 path: U.S. rate reductions H1 -17.3, Q3 -18.0, Q4 -8.9 against U.S. disposal results -9.4, -11.1, -27.7 [calc]",
    "P74, p. 126; P62, p. 54; P254, p. 14; P234, pp. 13 to 14",
    "The reductions were set in earlier quarters (\"from previous quarters\") on the residual evidence then available and on expected gains from new sales channels (\"car sales channel diversification and acceleration of our retail sales expansion\", P234); losses arose on cars sold after residuals weakened late in the year, and rates are \"adjusted prospectively\" (P62, p. 45), so the two statements can describe different parts of the year",
    "Depreciation rates were lowered in every 2013 period while cars sold realized less than book value, so the book value of cars still held at 31 December 2013 may exceed what they will realize and cost may reach later periods as disposal losses, which enter depreciation on sale",
    "E22 (rate changes every year); E9 (holding-period optimization with Dollar Thrifty); E24 (fleet cost revised); Q4 2013 derived on mixed bases (context sheet, Read first item 2)",
    "Q4 2013 rate-change and disposal detail, age and residual assumptions of the year-end fleet: not in pack (searched P74, P62, P254, P295, P296)",
    "P1")
row("F3-C5-01", "C5 Fleet depreciation rate down while fleet reinvestment up", "FY2010 to FY2013",
    "Fleet depreciation / average gross fleet 0.1629, 0.1527, 0.1460, 0.1447, lowest in FY2013 and down three years running; net fleet capex / fleet depreciation 0.515, 0.886, 1.203, 1.241, highest in FY2013 and up three years running; rate-change effect -18.2, -130.1, -39.6 (FY2011 to FY2013), FY2012 equal to 28.9% of pre-tax income as originally reported [calc]. Triggers (a) and (b)",
    "P1, IS_A, BS_A, CF_A; P16, p. 125; P45, p. 113; P74, p. 126",
    "Fleet growth and acquisitions (Donlen lease vehicles with contracted residuals, Dollar Thrifty) raise gross fleet and purchases; strong 2011 to 2012 residuals and longer holding periods justify lower rates; on the revised FY2012 base the FY2013 rate (0.1449) is level with FY2012 as revised (0.1448) [calc]",
    "Each year's estimate change moved depreciation down while 2013 disposal results turned to losses, so reported fleet cost may run below eventual realized cost and the gap would surface later",
    "E2, E9, E16 (fleet acquired); E22 (rate changes); E24",
    "Fleet mix (program versus non-program, Donlen share) and average holding period by year: not found in Notes 2 and 8 or MD&A depreciation sections searched",
    "P2")
row("F3-C8-02", "C8 Stated car holding-period range lengthened; other stated lives changed", "FY2011 to FY2013",
    "\"Cars | 4 to 26 months\" (FY2011), \"Cars | 4 to 28 months\" under \"Useful lives are as follows:\" (FY2012), \"Cars | 4 to 36 months\" under \"Holding periods are as follows:\" (FY2013); FY2013 also \"Capitalized internal use software | 1 to 10 years\" (was 1 to 15), \"Buildings | 5 to 50 years\" (was 3 to 50), \"Other intangible assets | 3 to 10 years\" (was 3 to 20). No change-in-estimate wording in any of 298 text files [calc, search]",
    "P11, p. 94; P39, p. 81; P68, p. 91",
    "The ranges describe the fleet and assets in place (Dollar Thrifty vehicles, longer-held cars) rather than a change in estimate; the software and intangible ranges shortened, which adds expense; Note 8 quantifies the rate changes",
    "A longer maximum holding period lowers monthly depreciation per car and its effect is not quantified apart from the rate changes; changes are prospective, so the depreciation series breaks without restatement",
    "E9 (\"optimization of fleet holding periods related to the integration of Dollar Thrifty\", P74); E22",
    "Depreciation effect of the holding-period extension: not in pack (searched P74, P68, P62, P254)",
    "P2")
row("F3-C2-01", "C2 Recurring adjustments labelled non-recurring or one-time", "Q1 FY2011 to Q4 FY2013",
    "Restructuring adjusted out in 16 of 16 quarters and acquisition related costs in 15 of 16 (Q1 FY2010 to Q4 FY2013); restructuring 49.1 (FY2012) to 100.2 (FY2013) [calc]; both listed each quarter under \"EXTRAORDINARY, UNUSUAL OR NON-RECURRING ITEMS\"; definition \"certain one-time charges\" in releases and the filed 10-K; 10-K expects relocation spending \"over the next two years\" while \"Relocation costs\" are adjusted out",
    "P271 to P295, INCOME MEASUREMENTS and Corporate EBITDA tables; P62, pp. 50 and 65; P77, pp. 134 to 135",
    "The non-recurring wording is the credit-agreement definition of Corporate EBITDA (\"As defined in the credit agreements for the senior credit facilities\"), not management's description; adjusted pre-tax income is the ASC 280 segment measure; restructuring is disclosed every quarter as a multi-year programme (\"incremental costs incurred directly supporting our business transformation initiatives\")",
    "Charges present every quarter and doubling in FY2013 are presented as one-time or non-recurring, so adjusted pre-tax income may overstate the recurring run-rate by those amounts; in filed documents Item 10(e) bars the non-recurring label for charges that occurred in the prior two years or are reasonably likely in the next two",
    "E9 (integration), E10; restructuring and relocation are not on the context sheet",
    "Management's basis for the one-time label in the filed MD&A (P62, p. 50 note (c)); Item 10(e)(1)(ii)(B) text not in pack",
    "P2")
row("F3-C3-01", "C3 Debt-charge label and definition changed; tax rate changed", "Q4 FY2012 to Q4 FY2013",
    "Q4 FY2012 \"non-cash debt charges\" \"Also includes $17.5 million of pre-acquisition interest and commitment fee expenses for interim financing\"; from Q4 FY2013 the line is \"Debt-related charges\", defined as \"debt-related charges relating to the amortization of deferred debt financing costs and debt discounts\"; normalized tax rate 34% (2012) to 35% (2013)",
    "P285, p. 10, line 291; P295, p. 2, line 36 and line 315; P287, p. 2, line 41; P295, line 817",
    "The new label fits a line that had included a cash item; the tax rate is management's \"estimate of our long-term tax rate\" and each year is shown at its own rate",
    "A line labelled non-cash included cash interest and fees in Q4 FY2012, then the label changed with no stated reason; the rate change shifts adjusted net income between years",
    "E13 (EPS numerator policy), E14 (RPD definition); the relabel is not on the context sheet",
    "Explanation or recast of the relabel: not found in P295, P296 (\"non-cash debt\", \"previously\", \"formerly\", \"renamed\", \"conform\", \"reclassif\")",
    "P3")
row("F3-C3-02", "C3 Q2 FY2012 amount carried under two categories in one release", "Q2 FY2013",
    "Table 1 shows Q2 2012 acquisition related costs of 4.5 (as in the Q2 FY2012 release); Table 5 of the same release puts that 4.5 on \"Integration expensess (d)\" and none on acquisition related costs, while its six-month 2012 column keeps 11.4 (6.9 + 4.5 [calc]) under acquisition related costs; Q2 2013 acquisition plus integration costs are 18.3 in Table 1 and 25.3 in the Corporate EBITDA non-recurring table [calc]",
    "P289, p. 2, line 41; p. 11, lines 374 to 375 and 405; p. 13, line 547; P281, p. 2, line 38",
    "A labelling slip in a furnished release with no effect on the adjusted total; the two reconciliations serve different measures (adjusted pre-tax income and the credit-agreement Corporate EBITDA), so category amounts can differ",
    "Boundaries between acquisition, integration and restructuring costs are not stable across tables, which makes growth in any one category hard to track",
    "E9",
    "Reconciliation of category amounts between the two tables: not found in P289",
    "P3")
row("F3-C3-03", "C3 New adjustment categories", "Q4 FY2012 to Q4 FY2013",
    "First appearances: Other (Q4 FY2012), Integration expenses (Q1 FY2013), Relocation costs and Impairment charges and other (Q3 FY2013) [calc]; row label \"Other unusual/non-recurring (c)\" (Q2 and Q3 FY2013); FY2013 amounts 40.0, 7.8, 44.0 and 50.7; \"Certain adjustments have been reclassified to conform with current period presentation\"; 0.5 of first-half relocation cost sat under another label [calc]",
    "P285, p. 2; P287, p. 2; P293, pp. 2, 10, 14; P295, p. 5",
    "Each new category matches a disclosed event (Dollar Thrifty integration, headquarters move, Simply Wheelz bankruptcy, convertible note conversion, pension withdrawal and Hurricane Sandy), and the prior periods had none",
    "The set of excluded items widened in FY2013, raising the gap between adjusted and GAAP pre-tax income; Integration and Relocation were not defined in the releases that introduced them",
    "E9, E10, E13",
    "Definitions in the introducing releases: not found in P287, P293; given later in the FY2013 10-K (P77, p. 135; P62, pp. 44 and 65)",
    "P3")
row("F3-C4-01", "C4 Prominence: adjusted measures lead", "Q1 FY2011 to Q4 FY2013",
    "First adjusted measure precedes the first GAAP measure in 10 of 12 headline blocks and 12 of 12 opening paragraphs; GAAP present in all 12 headline blocks and opening paragraphs [calc]; titles such as \"Nine Consecutive Quarters of Record Adjusted Pre-Tax Income\"",
    "P271 to P295, p. 1 (first 60 words in Table 5c); P293, p. 1",
    "Every release states GAAP pre-tax income and EPS in the bullets and first paragraph with full reconciliations, and the adjusted measure is the company's segment measure",
    "The ordering gives adjusted figures more prominence than GAAP figures; releases furnished under Item 2.02 are subject to the equal-or-greater-prominence requirement [unverified: rule text not in pack]",
    "none",
    "Item 10(e)(1)(i)(A) and Form 8-K Item 2.02 instruction text; any SEC comment correspondence: not in pack",
    "P3")
row("F3-B4-01", "B4 GMI rising for three pairs", "FY2013 / FY2012",
    "GMI 0.8190, 0.8484, 0.9559, 0.9942 (1.0001 against FY2012 as revised); cost-line margin 0.1529, 0.1867, 0.2201, 0.2302, 0.2316 [calc]. Triggers (a) and (b)",
    "P1, IS_A and EXTRA (direct operating; depreciation of revenue earning equipment and lease charges)",
    "Margin rose every year; GMI approaches 1 from below as recovery gains level off",
    "Margin gains have flattened while fleet depreciation-rate reductions (130.1 in FY2012, 39.6 in FY2013) were part of the cost line, so the margin level partly rests on estimate changes",
    "E22, E24 (vendor incentives moved into fleet cost), E9",
    "Cost-line margin excluding rate changes and disposal adjustments: inputs in pack (Note 8), not computed here",
    "P3")
row("F3-B1-01", "B1/B2 Balance-sheet and cash-flow accruals diverge; residuals not traced", "FY2010 to FY2013",
    "Balance-sheet minus cash-flow accrual numerator -180.4, 414.8, 600.0, 726.6 (-0.0108 to 0.0304 of average total assets); FY2013 receivables line differs by 408.7, of which 260.0 lower fleet-sale receivables and 45.9 provision, leaving 102.8 (118.5 after property-sale receivables) not traced; prepaid and other 205.7; accrued liabilities -101.0 [calc]",
    "P1, BS_A, CF_A, EXTRA; P66, pp. 75 and 80 to 81",
    "Acquisitions and de-consolidation (E2, E9, E15, E16), fleet-related non-cash investing balances, restricted cash (investing) and deferred taxes (non-current) sit in the balance-sheet measure and not in operating cash flow; FY2010 payables difference lines up with fleet purchases held in payables",
    "Part of the FY2013 movement in receivables and accrued liabilities is not traced to a disclosed line, so some operating balance changes may sit outside operating cash flow",
    "E2, E9, E10, E15, E16; tie-out W1",
    "Receivables and accrued-liability rollforwards; balances removed with the China entities: not found in P70, P66",
    "P3")
row("F3-C17-01", "C17 Cash from operations and free cash flow relative to income at series low", "FY2013",
    "CFO / income 11.41, 11.18, 10.37; FCF / income 9.97, 9.89, 9.46 (FY2011 to FY2013; FY2009 and FY2010 were losses); FCF after net fleet capex / income 1.78, -0.34, 0.70 [calc]. Trigger (a)",
    "P1, CF_A and IS_A",
    "Ratios near 10 are structural: fleet depreciation is an operating add-back and fleet purchases are investing; income grew faster than cash flow in the highest-income year, with deferred tax up to 241.3",
    "Free cash flow after fleet reinvestment has been below income since FY2012 and was negative in FY2012, so reported income is not matched by cash after fleet replacement",
    "E9; E24 (FY2012 CFO revised -8.3); tie-out W1",
    "Fleet financing flows and program-car repurchase receipts: partly in P295 Table 7",
    "P3")
row("F3-C7-01", "C7 Interest capitalized referenced but not quantified", "FY2011 to FY2013",
    "\"Interest (net of amounts capitalized)\" in each cash flow statement and \"net of amounts capitalized\" in MD&A; \"capitalized interest\", \"interest capitalized\" and \"construction in progress\" return 0 hits in 298 files [calc, search]",
    "P66, p. 81; P62, p. 66; P9, p. 90; P37, p. 78",
    "Capitalized interest is nil or immaterial and the caption is standard wording",
    "If interest is capitalized in amounts that matter, part of interest cost is deferred to the balance sheet without a stated amount",
    "none",
    "Interest incurred and capitalized by year (ASC 835-20 disclosure) [unverified: standard not in pack]; not in pack",
    "P3")
row("F3-C17-02", "C17 Company free cash flow excludes DTG items in FY2012", "FY2012 and FY2013",
    "\"(1) 2012 free cash flow excludes certain DTG acquisition related items of approximately $129.6 million as previously disclosed.\"; FY2013 free cash flow \"$448.7 million an increase of $293.6 million\"",
    "P295, p. 2 and Table 7, line 599",
    "One-off acquisition-related cash items were removed so the years compare on operating terms, and the exclusion is footnoted",
    "The direction of the excluded items is not stated, so the effect on the reported FY2013 increase cannot be read from the release; the company measure also differs from the step 7 measure",
    "E9",
    "Composition of the 129.6: not found in P295, P296",
    "P4")
row("F3-B4-02", "B4 SGI highest in series", "FY2013 / FY2012",
    "SGI 1.1941 against 1.0649 to 1.0973 in earlier pairs [calc]. Trigger (a)",
    "P1, IS_A",
    "Full year of Dollar Thrifty in FY2013 against 43 days in FY2012",
    "Post-acquisition growth is the setting in which the SGI term was estimated as a pressure indicator",
    "E9, E10, E15",
    "Revenue growth excluding Dollar Thrifty: release attributes U.S. growth \"primarily due to Dollar Thrifty\" (P295, p. 1); amount not found",
    "P4")
row("F3-B4-03", "B4 SGAI lowest in series", "FY2013 / FY2012",
    "SGAI 0.9051 (0.8846 against FY2012 as revised); SG&A / revenue 0.1048 (FY2012; 0.1073 revised) to 0.0949 (FY2013) [calc]. Trigger (a): lower SGAI raises M",
    "P1, IS_A; P66, p. 76",
    "Dollar Thrifty synergies and scale; FY2012 SG&A carried Dollar Thrifty acquisition costs",
    "SG&A fell as a share of revenue in a period when costs were reclassified between SG&A and fleet cost (E24)",
    "E9, E24",
    "SG&A excluding acquisition and integration costs by year: partly in release Table 5 (P285, P295)",
    "P4")
row("F3-B5-01", "B5 F-score above 1.0 on workbook mapping; soft assets rising", "FY2011 to FY2013",
    "F-score 1.768, 1.850 (1.8497), 1.766; soft assets 0.7959, 0.8764, 0.9154, 0.9212 (FY2010 to FY2013), highest in FY2013 and up three years; largest contributions soft assets (+1.82 in FY2013) and issuance (+1.029); fleet in PP&E gives 0.573, 0.620, 0.566 [calc]. Triggers (a) and (b) on soft assets",
    "P1, BS_A and CF_A",
    "The rental fleet (0.55 to 0.58 of assets) is outside the P1 PP&E line, and goodwill and intangibles rose from 0.1672 to 0.2308 of assets with Dollar Thrifty; issuance is 1 for a company that refinances fleet debt continuously",
    "A larger share of assets rests on valuation estimates (goodwill, intangibles, fleet residuals), mostly from acquisitions",
    "E2, E9, E21",
    "Goodwill and trade-name impairment testing (Note 3, in pack; F4)",
    "P4")
row("F3-B6-01", "B6 Cash sales growth highest in series", "FY2013",
    "Change in cash sales 0.0674, 0.0886, 0.2737 against FY2013 revenue growth 0.1941 and receivables growth -0.1982; FY2013 cash-flow accruals -0.1355 and RSST 0.0156 [calc]. Trigger (a)",
    "P1, IS_A, BS_A, EXTRA",
    "Fleet-sale receivables (investing) fell 260.0, Dollar Thrifty contributed a full year and the China entities left the balance sheet; accruals are low, so the step 4 pairing with high accruals does not arise",
    "The part of the receivables decline not traced to a line (F3-B1-01) would lift cash sales without a cash counterpart in operations",
    "E9, E15",
    "Receivables rollforward (F2, A1 to A8)",
    "P4")
row("F3-C19-01", "C19 Cash-flow classification revisions for fleet lease payments", "Q1 2010 to Q3 2010 comparatives",
    "\"we have revised net cash provided by operating activities and net cash used in investing activities ... due to a gross-up of cash lease payments relating to our revenue earning equipment\"; parent-only return of capital moved to investing; amounts for the gross-up not stated",
    "P91, p. 7; P131 (Q3 2011 10-Q Note 2); P37, p. 138",
    "Presentation corrections that the company disclosed when made",
    "Classification of fleet-related cash between operating and investing was corrected more than once, so operating cash flow trends across 2010 may include classification effects",
    "E1, E12, E17 (F1-C15-3)",
    "Amounts of the gross-up: not found in P91, P131",
    "P4")

for r_ in R:
    for k, v in r_.items():
        assert "\u2014" not in v, (r_["ID"], k)
md = io.StringIO()
md.write("| " + " | ".join(COLS) + " |\n|" + "---|" * len(COLS) + "\n")
for r_ in R:
    md.write("| " + " | ".join(r_[c].replace("|", r"\|") for c in COLS) + " |\n")
cs = io.StringIO()
w = csv.writer(cs, lineterminator="\n")
w.writerow(COLS)
for r_ in R:
    w.writerow([r_[c] for c in COLS])
open("ledger_md.txt", "w", encoding="utf-8").write(md.getvalue())
open("ledger-F3.csv", "w", encoding="utf-8").write(cs.getvalue())
from collections import Counter
print(len(R), "rows", Counter(r_["Priority"] for r_ in R))
```

**assemble.py**

```python
# assemble.py : build F3-output.md from the parts, the generated tables, the ledger and the scripts; count figures
import re, os, shutil
OUT_DIR = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\tests\hertz-fy2013\runs\v0.2-claude-code"
body = "".join(open(p, encoding="utf-8").read() for p in ["body_part1.md", "body_part2.md", "body_part3.md", "body_part4.md"])
body = body.replace("section 8.1", "section 7")

tables = open("out_tables.md", encoding="utf-8").read()
blocks = {}
for m in re.finditer(r"\n(Table (\w+)\. [^\n]*)\n\n((?:\|[^\n]*\n)+)", tables):
    blocks[m.group(2)] = m.group(1) + "\n\n" + m.group(3).rstrip("\n")
for k in ["1a", "1b", "2", "3", "5a", "7a", "7b"]:
    body = body.replace(f"<<Table {k}>>", blocks[k])

rows = []
for line in open("w60.txt", encoding="utf-8").read().splitlines():
    q, pid, hg, ha, pg, pa, w = line.split("|", 6)
    first_h = "adjusted" if int(ha) < int(hg) else "GAAP"
    first_p = "adjusted" if int(pa) < int(pg) else "GAAP"
    rows.append(f"| {q} | {pid}, p. 1 | yes | {first_h} | yes | {first_p} | \"{w}\" |")
body = body.replace("<<Table 5c rows>>", "\n".join(rows))
body = body.replace("<<LEDGER_MD>>", open("ledger_md.txt", encoding="utf-8").read().rstrip("\n"))
body = body.replace("<<LEDGER_CSV>>", open("ledger-F3.csv", encoding="utf-8").read().rstrip("\n"))

code = []
for f in ["f3_load.py", "f3_compute.py", "f3_nongaap.py", "f3_search.py", "f3_extra.py", "f3_fleetq.py", "f3_tables.py", "f3_ledger.py", "assemble.py"]:
    code.append(f"**{f}**\n\n```python\n" + open(f, encoding="utf-8").read().rstrip("\n") + "\n```")
body = body.replace("<<CODE>>", "\n\n".join(code))

# figure counts: numeric cells in computation-table rows (section 4) by row mark; unverified tags in the whole text
sec4 = body[body.index("## 4. Computation tables"):body.index("## 5. Text found")]
num_rx = re.compile(r"(?<![A-Za-z])-?\d[\d,]*\.?\d*")
calc = copied = 0
for line in sec4.splitlines():
    if not line.startswith("|") or line.startswith("|---") or line.startswith("| Line") or line.startswith("| Quarter") or line.startswith("| Category"):
        continue
    cells = [c.strip() for c in line.strip("|").split("|")]
    mark = cells[-1]
    vals = cells[1:-1]
    n = sum(len(num_rx.findall(v)) for v in vals if not v.startswith('"'))
    if mark.startswith("[calc") or mark == "[formula]":
        calc += n
    elif mark.startswith("[P") or mark.startswith("[release"):
        copied += n
unver = len(re.findall(r"\[unverified", body.split("## 9. Code")[0]))
L, Rb = "<" + "<", ">" + ">"
body = body.replace(L + "X" + Rb, str(copied)).replace(L + "Y" + Rb, str(calc)).replace(L + "Z" + Rb, str(unver))
body = body.replace("Figures: " + str(copied), "Figures (computation tables): " + str(copied))

assert "\u2014" not in body.split("## 9. Code")[0], "em-dash in output"
for w in ["fraud", "manipulation", "aggressive", "red flag", "suspicious", "concerning"]:
    hits = [m.start() for m in re.finditer(w, body.split("## 9. Code")[0], re.I)]
    print(w, len(hits))
open(os.path.join(OUT_DIR, "F3-output.md"), "w", encoding="utf-8").write(body)
shutil.copy("ledger-F3.csv", os.path.join(OUT_DIR, "ledger-F3.csv"))
print("copied", copied, "calc", calc, "unverified", unver, "chars", len(body), "words", len(body.split()))
```

Verification: 17 items run, 18 ledger rows (P1 1, P2 3, P3 8, P4 6), 11 could not run. Figures (computation tables): 148 copied, 842 calculated, 6 unverified. Units: USD, millions. Framework: US GAAP. Context sheet: used.

**Candidates for review, not findings.**
