# مصفوفة الوصول والتحقق المرجعي للفصل الرابع عشر

التاريخ: 2026-07-21

```text
VERSION                 = 0.18.0-dev
CHAPTER                  = 14
TOPIC                    = BARBAN--DAVENPORT--HALBERSTAM
REFERENCE-PINNING        = PARTIAL
PASS-FOR-AUTHORING       = NO
```

## قاعدة التحقق

نميز بين ثلاث درجات:

1. `TEXT-VERIFIED`: فُحص نص الورقة أو المبرهنة نفسها.
2. `BIBLIOGRAPHY-VERIFIED`: ثبتت بيانات النشر وDOI والصفحات، لكن نص المبرهنة لم يُفحص.
3. `SECONDARY-FORMULA-ONLY`: ظهرت الصيغة في مصدر لاحق موثوق، ولا تكفي وحدها لإسناد الصياغة الأصلية.

## المصفوفة

| المصدر | البيانات | حالة الوصول | ما ثبت | ما بقي |
|---|---|---|---|---|
| Davenport--Halberstam, *Primes in arithmetic progressions*, Michigan Math. J. 13 (1966), 485--489 | DOI وبيانات النشر مثبتة | `BIBLIOGRAPHY-VERIFIED` | وجود الورقة، السنة، المجلد، الصفحات | نص المبرهنة، التطبيع، مجال `Q` |
| Corrigendum, Michigan Math. J. 15 (1968), 505 | بيانات النشر مثبتة | `BIBLIOGRAPHY-VERIFIED` | وجود التصحيح ومكانه | مضمون التصحيح وأثره على الصياغة |
| Gallagher, *The large sieve*, Mathematika 14 (1967), 14--20 | DOI وصفحة الناشر مثبتان | `BIBLIOGRAPHY-VERIFIED` | الورقة ومدخل الغربال الكبير | موضع النتيجة الدقيقة ذات الصلة بالـBDH |
| Gallagher, *Bombieri's mean value theorem*, Mathematika 15 (1968), 1--6 | نص الملخص والمراجع متاحان | `PARTIAL-TEXT-VERIFIED` | الورقة تعرض برهانًا قصيرًا لمبرهنة Bombieri وتُحيل إلى Barban وGallagher | لا تُعامل كصيغة BDH التقاربية |
| Montgomery, *Primes in arithmetic progressions*, Michigan Math. J. 17 (1970), 33--39 | بيانات المؤلف والمجلة والصفحات مثبتة | `BIBLIOGRAPHY-VERIFIED` | المرجع الأساسي للصيغة التقاربية | النص الكامل، الحد الرئيسي، الخطأ، مجال `Q` |
| Hooley I, J. reine angew. Math. 274/275 (1975), 206--223 | DOI وبيانات النشر مثبتة | `BIBLIOGRAPHY-VERIFIED` | بداية سلسلة Hooley | المبرهنة المستعملة فعلًا وصيغتها |
| Hooley III, J. London Math. Soc. (2) 10 (1975), 249--256 | DOI وبيانات النشر مثبتة | `BIBLIOGRAPHY-VERIFIED` | الجزء الثالث من السلسلة | هل يلزم للفصل الأساسي أم للتوسعات فقط |
| Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences* (2025) | النص المفتوح متاح | `TEXT-VERIFIED-MODERN` | يميز بين variance على مقطع dyadic وصيغ تقاربية عامة ويثبت أن الأدبيات الحديثة تفصل التطبيع بعناية | لا يُستعمل بدل الأوراق الأصلية في الإسناد التاريخي |

## القرار المنهجي

- تبقى الصيغة الأساسية المرشحة حدًا علويًا فقط.
- لا تُسند الصيغة التقاربية إلى Montgomery أو Hooley بصياغة نهائية قبل فحص النص الكامل.
- لا يُحجز رقم نتيجة في السجل بعد.
- لا يبدأ متن LaTeX للفصل بعد.

```text
PASS-FOR-REFERENCE-PINNING = PARTIAL
PASS-FOR-AUTHORING         = NO
```
