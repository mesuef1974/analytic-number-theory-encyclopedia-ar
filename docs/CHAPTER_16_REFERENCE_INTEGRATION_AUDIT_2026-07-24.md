# تدقيق دمج مراجع الفصل السادس عشر

آخر تحديث: 2026-07-24

```text
CHAPTER               = 16
VERSION               = 0.20.0-dev
BRANCH                = agent/chapter-16-sieve-applications-prime-gaps-v0.20.0
REFERENCE-INTEGRATION = PASS
BIBTEX-KEYS           = 7
CITED-RESULTS         = 5 THEOREMS + 1 HISTORICAL NOTE
BROKEN-CITEDRESULT    = 0
PDF-BUILD             = PENDING / NO REMOTE CI STATUS
RELEASE-READY         = NO
```

## الملفات

- `manuscript/chapter-16-bibliography.bib`
- `manuscript/preamble.tex`
- `volumes/volume-01-foundations/chapters/chapter-16-sieve-applications-prime-gaps.tex`

## المفاتيح المثبتة

1. `Brun1919TwinPrimeReciprocals`
2. `Chen1973PrimePlusP2`
3. `GoldstonPintzYildirim2009PrimesTuplesI`
4. `Zhang2014BoundedGaps`
5. `Maynard2015SmallGaps`
6. `Polymath2014SelbergVariants`
7. `Polymath2015SelbergVariantsErratum`

## التحقق النصي

- أضيف ملف الفصل إلى `biblatex` في `manuscript/preamble.tex`.
- استُبدلت جميع أوامر `\citedresult` الناقصة بأوامر ذات وسيط مرجعي صريح.
- أضيفت إحالة تاريخية مباشرة إلى برون في نتيجة تقارب مجموع المقلوبات.
- رُبط حد Polymath8b بالمقالة الأصلية وتصويبها المنشور.
- لم تُنسب إلى Tao ورقة منشورة مستقلة غير موجودة؛ سُجل التطوير المستقل تاريخيًا، وجُعل Maynard وPolymath8b مرجعي الصياغة المنشورة.

## الحكم

اجتاز دمج المراجع التدقيق النصي والحوكمي. لا يمكن تسجيل `PDF-BUILD = PASS` من GitHub حاليًا لأن الرأس لا يحمل أي حالة CI منشورة؛ يلزم بناء XeLaTeX/Biber كامل قبل إغلاق تدقيق ما بعد التأليف.
