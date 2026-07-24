# سجل نتائج الفصل الخامس عشر

آخر مراجعة: 2026-07-24

```text
CHAPTER                = 15
VERSION                = 0.19.0-dev
AUTHORING              = NOT-STARTED
PASS-FOR-AUTHORING     = PENDING-FINAL-GATE
CHAPTER-STATE          = PRE-AUTHORING
RELEASE-READY          = NO
```

| المعرّف | النتيجة | الحالة المحجوزة | المصدر أو البرهان |
|---|---|---|---|
| `ANT-DEF-15-01` | بيانات الغربال المجردة: \(P(z)\)، و\(S(\mathcal A,\mathcal P,z)\)، والتفكيك \(|\mathcal A_d|=Xg(d)+r_d\) | `DEFINITION / RESERVED` | اصطلاح الفصل المثبت في تدقيق التطبيع |
| `ANT-LEM-15-01` | متراجحة المربع: \(S(\mathcal A,\mathcal P,z)\le\sum_{n\in\mathcal A}(\sum_{d\mid(n,P(z))}\lambda_d)^2\) عند \(\lambda_1=1\) | `PROVED-HERE / RESERVED` | برهان مباشر من كون الوزن يساوي 1 على العناصر المنخولة |
| `ANT-THM-15-01` | الحد العلوي المنتهي لغربال سيلبرغ: \(S\le X/G(R,z)+\sum_{d<R^2}3^{\omega(d)}|r_d|\) | `PROVED-HERE / RESERVED` | تحويل الصورة التربيعية، كوشي--شفارتس، واختيار سيلبرغ الأمثل |
| `ANT-THM-15-02` | تقدير مقام سيلبرغ في بعد \(\kappa\): \(G(z,z)=e^{\gamma\kappa}V(z)^{-1}/\Gamma(\kappa+1)\,(1+O(1/\log z))\) | `CITED / COMPOSITE-INPUT / RESERVED` | Halberstam--Richert ومعالجات الغربال القياسية؛ الموضع الدقيق يثبت في BibTeX والمتن |
| `ANT-THM-15-03` | اللمّة الأساسية العامة للغربال في صيغة واحدة مختارة | `CITED / COMPOSITE-INPUT / RESERVED` | Opera de Cribro أو Diamond--Halberstam--Galway بعد تثبيت الصياغة النهائية |
| `ANT-PROP-15-01` | الكثافة المحلية للأزواج \(n,n+h\): \(\rho_h(p)=2\) إذا \(p\nmid h\)، و\(1\) إذا \(p\mid h\)، مع انعدام الحالة الفردية بعد غربلة 2 | `PROVED-HERE / RESERVED` | حساب فئات البواقي ومبرهنة الباقي الصيني |
| `ANT-PROP-15-02` | للحالة الزوجية \(h\ne0\)، يكون البعد الغربالي \(\kappa=2\) و\(V_h(z)\asymp_h(\log z)^{-2}\) | `PROVED-HERE / RESERVED` | تحليل العوامل المحلية مع مبرهنة ميرتنز |
| `ANT-THM-15-04` | لكل ثابت زوجي \(h\ne0\): \(S_h(x,z)\ll_h x/(\log z)^2\) بانتظام في \(3\le z\le x^{1/4}\) | `PROVED-HERE / RESERVED` | `ANT-THM-15-01` و`ANT-THM-15-02` وحساب البواقي المحلي |
| `ANT-DIAG-15-01` | عائق التكافؤ: بيانات القواسم المحلية التقليدية لا تميز وحدها بما يكفي بين تكافؤ عدد العوامل الأولية | `DIAGNOSTIC / CITED / RESERVED` | Opera de Cribro، ومعالجة Selberg/Polymath الحديثة مع حدود الادعاء |

## حدود التسجيل

- لا تسجل حدسية الأوليات التوأم أو أي حد سفلي لعدد الأزواج الأولية.
- لا تسجل الفجوات المحدودة نتيجة للفصل.
- لا تسجل Brun--Titchmarsh ضمن المسار المركزي.
- لا تسجل صيغ \(F_\kappa(s),f_\kappa(s)\) قبل اختيار تطبيعها النهائي.
- لا تصبح النتائج `ACTIVE` قبل تدقيق ما بعد التأليف.

```text
RESULTS-RESERVED       = 9
MATHEMATICAL-BLOCKERS  = 0
TEXTUAL-BLOCKERS       = 0
PASS-FOR-AUTHORING     = PENDING-FINAL-GATE
```
