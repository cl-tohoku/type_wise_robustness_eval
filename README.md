# type_wise_robustness_eval

## 概要
type_wise_robustness_evalは機械翻訳システムの「言語現象に対する頑健性測定」のためのデータセットです。

このデータセットは[MTNTデータセット](https://www.cs.cmu.edu/~pmichel1/mtnt/) v1.1において提供された日本語(Ja)-英語(En)対訳ペアについて、以下の言語現象が見られる対訳ペアを集約することで作成されたデータセットです。各言語現象に対するデータセットは、「MTNTデータセットからの原文」および「言語現象に該当する箇所を置換した文」の2文からなるペアで構成されています。

このデータセットが対象としている言語現象は以下のとおりです。

```
* 固有名詞 (proper)
* 名詞の省略 (noun_ellipsis)
* かな表記 (kana)
* 非正規形 (unnormalized)
```

## 構成

このリポジトリは以下の構成からなっています。

```
.
├── README.md
├── orig.ph.clean.ja
├── orig.ph.noisy.ja
├── clean.ja.placeholder
├── noisy.ja.placeholder
├── ref.clean.en
├── ref.noisy.en
├── proper (固有名詞)
│   ├── orig.ph.ja (MTNT原文コーパス)
│   ├── rep.ph.ja (置換後文コーパス)
│   ├── ja.placeholder (絵文字プレースホルダ)
│   ├── orig.en (原文参照訳)
│   └── rep.en (置換後参照訳)
├── noun_ellipsis (名詞の省略)
│   ├── orig.ph.ja (MTNT原文コーパス)
│   ├── rep.ph.ja (置換後文コーパス)
│   ├── ja.placeholder (絵文字プレースホルダ)
│   └── ref.en (参照訳)
├── kana (かな表記)
│   ├── orig.ph.ja
│   ├── rep.ph.ja
│   ├── ja.placeholder
│   └── ref.en
└── unnormalized (非正規形)
│   ├── orig.ph.ja
│   ├── rep.ph.ja
│   ├── ja.placeholder
│   └── ref.en
└── scripts
    └── replace_ph.py

```

本データセット中のMTNT原文、および置換後文中の絵文字/顔文字は[nagisaツールキット](https://github.com/taishi-i/nagisa) を用いて特殊トークン`<PH>`に置換されています。以下のコマンドによりプレースホルダを復元することができます。

```python scripts/replace_ph.py $DIR_NAME/{orig, rep}.ph.ja $DIR_NAME/ja.placeholder > $OUT_FILE```

## データセットの規模

本データセットの言語現象毎の文対数は以下のとおりです。

| 言語現象 | 文対数 |
----|---- 
| 固有名詞 | 290 |
| 名詞の省略 | 97 |
| かな表記 | 77 |
| 非正規形 | 72 |