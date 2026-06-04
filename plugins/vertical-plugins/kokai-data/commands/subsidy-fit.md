---
name: subsidy-fit
description: /subsidy-fit <13-digit 法人番号> <J-Grants subsidy_id> — generate a 3-axis fit signal for a Japanese company x subsidy pair
---

# /subsidy-fit

Run the `subsidy-fit-jp` agent workflow on a Japanese company × subsidy pair.

Arguments:

- `<corporate_number>`: 13-digit Japanese 法人番号
- `<subsidy_id>`: J-Grants subsidy ID

The output is a **3-axis fit signal** (regional / industry / scale):

1. Regional fit: target_area_search matches company prefecture
2. Industry fit: subsidy industry tag aligns with company industry
3. Scale fit: company employee count / capital fits subsidy target range

Each axis returns `fit` / `partial fit` / `no fit` / `insufficient data` with cited reasoning.

## Boundary

- Output is **signal / 確認材料 / context**, NOT eligibility judgment.
- Final 適格性 / 申請可否 verification requires a certified Japanese 士業 (行政書士 / 中小企業診断士).
