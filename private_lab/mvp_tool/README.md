# MVP Tool (Phase-1)

被动资产发现最小实现：`公司名 -> 归属资产清单（证据 + 置信度）`。

## Usage
```bash
python3 private_lab/mvp_tool/mvp_asset_discovery.py --company google --out private_lab/mvp_tool/output.google.json
python3 private_lab/mvp_tool/evaluate.py --pred-json private_lab/mvp_tool/output.google.json --gold private_lab/mvp_tool/gold_sets/google.txt --n 50
```

## Notes
- 默认仅使用 profile 种子与规则，不会主动攻击。
- `--with-crtsh` 可启用证书透明度被动查询（网络可用时）。
- 标注流程自动化仍是 TODO（见治理文档）。
