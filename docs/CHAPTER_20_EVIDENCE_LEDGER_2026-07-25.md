# سجل أدلة الفصل العشرين — 2026-07-25

## الحالة

```text
CHAPTER              = 20
VERSION              = 0.24.0-dev
MODE                 = EVIDENCE-FIRST / PRE-AUTHORING
LEDGER               = OPEN / NOT FROZEN
AUTHORING            = BLOCKED
RESULTS              = RESERVED / NON-CITABLE
LITERATURE-CUTOFF    = 2026-07-25
```

هذا سجل افتتاحي لا يمنح أي مصدر حالة `CITED` بعد. لا تنتقل مادة إلى خريطة البرهان النهائية قبل تثبيت الطبعة والموضع والصيغة والتطبيع.

## نطاق الفصل

1. الفضاء العلوي وفعل `SL_2(Z)` والزمر الت合同ية الأساسية.
2. الأشكال المعيارية الهولومورفية، أشكال الحدبة، وتوسعات فورييه.
3. حاصل الضرب الداخلي لبيترسون ومؤثرات Hecke ضمن مستوى وتطبيع محددين.
4. أشكال مااس الحدبية، مؤثر لابلاس، والتوسع Fourier--Whittaker.
5. مجاميع Kloosterman وتحويلات Bessel بوصفها لغة صيغ التتبع.
6. صيغة Petersson وصيغة Kuznetsov، ومدخل محدود إلى صيغة Selberg.
7. التطبيقات التحليلية تُذكر بوصفها جسورًا للفصل 21، لا تُستبق براهين دون التحدب أو لانجلاندز.

## قائمة المصادر المرشحة للتحقق

| الرمز | المصدر المرشح | الدور المتوقع | الحالة |
|---|---|---|---|
| E20-01 | Diamond--Shurman, *A First Course in Modular Forms* | الأساس الهولومورفي، الفضاءات، مؤثرات Hecke | `CANDIDATE / LOCATOR-PENDING` |
| E20-02 | Miyake, *Modular Forms* | الصياغة الكلاسيكية والتفاصيل البنيوية | `CANDIDATE / LOCATOR-PENDING` |
| E20-03 | Iwaniec, *Spectral Methods of Automorphic Forms* | أشكال مااس والتحليل الطيفي وصيغ التتبع | `CANDIDATE / LOCATOR-PENDING` |
| E20-04 | Iwaniec--Kowalski, *Analytic Number Theory* | الجسر إلى التطبيقات التحليلية ومجاميع Kloosterman | `CANDIDATE / LOCATOR-PENDING` |
| E20-05 | Hejhal, *The Selberg Trace Formula for PSL(2,R)*, I--II | صيغة Selberg والتطبيعات الطيفية | `CANDIDATE / LOCATOR-PENDING` |
| E20-06 | أوراق Petersson الأصلية | صيغة الأثر الهولومورفية | `PRIMARY / BIBLIOGRAPHY-PENDING` |
| E20-07 | ورقة Kuznetsov الأصلية | صيغة الأثر غير الهولومورفية | `PRIMARY / BIBLIOGRAPHY-PENDING` |
| E20-08 | أعمال Selberg الأصلية/المجمعة | صيغة الأثر والطيف | `PRIMARY / BIBLIOGRAPHY-PENDING` |

## اكتشافات Consensus الأولية

أُجريت في 25 يوليو 2026 ثلاثة استعلامات مستقلة عن صيغ Kuznetsov وPetersson وSelberg. جرى استدعاء السجل الكامل لكل نتيجة أدناه بعد البحث، وفق قاعدة Consensus. هذه السجلات أدوات اكتشاف فقط ولا تحل محل النص الأصلي أو موضع المبرهنة.

| الرمز | السجل | البيانات المسترجعة | الحالة |
|---|---|---|---|
| C20-01 | [Kuznetsov's Trace Formula and the Hecke Eigenvalues of Maass Forms](https://consensus.app/papers/kuznetsovs-trace-formula-and-the-hecke-eigenvalues-of-li-knightly/fff6daeba5f95bbd84a521d529f62759/?utm_source=chatgpt) | Charles Li وAndrew H. Knightly، 2012، 69 استشهادًا في سجل Consensus | `CONSENSUS-DISCOVERED / PRIMARY-LOCATOR-PENDING` |
| C20-02 | [A relative trace formula proof of the Petersson trace formula](https://consensus.app/papers/a-relative-trace-formula-proof-of-the-petersson-trace-knightly-li/f14270f8796c5a96a98e28818bc94c4d/?utm_source=chatgpt) | Andrew H. Knightly وCharles Li، 2006، *Acta Arithmetica* 122، 297--313، 22 استشهادًا | `CONSENSUS-FETCHED / THEOREM-3.9-TO-VERIFY` |
| C20-03 | [The Selberg Trace Formula for PSL(2,R), Volume I](https://consensus.app/papers/the-selberg-trace-formula-for-psl2-volume-i-hejhal/a7208ee817515bc58e52d86ca1585f74/?utm_source=chatgpt) | D. Hejhal، 1976، 185 استشهادًا؛ الملخص غير متاح في السجل | `CONSENSUS-FETCHED / FULL-TEXT-REQUIRED` |

### حدود الاستخدام

- لا تعتمد أرقام الاستشهادات بوصفها معيار صحة.
- لا تعتمد مقتطفات Consensus لإثبات الثوابت أو التطبيعات.
- لا تُرفع أي نتيجة إلى `CITED` قبل مطابقة DOI/الناشر والنص الكامل.
- صيغة Petersson المذكورة في C20-02 تخص مستوى ووزنًا وشخصية محددة؛ لا تُعمم قبل قراءة Theorem 3.9 كاملًا.
- سجل Hejhal لا يحتوي ملخصًا، ولذلك لا يقدم دليلًا نصيًا على أي صيغة.

## اختبارات قبول المصدر

- تطابق تعريف الوزن والمستوى والشخصية.
- تثبيت قياس القطع الزائد وتطبيع حاصل الضرب الداخلي.
- تثبيت إشارة مؤثر لابلاس ومعلمة الطيف.
- تثبيت تطبيع معاملات فورييه وHecke.
- تثبيت تعريف مجموع Kloosterman وعوامل Bessel.
- فصل الصيغة الدقيقة عن النسخة التمهيدية أو التخطيطية.
- منع الاعتماد على نتيجة لاحقة من الفصل 21 لإثبات مدخل في الفصل 20.

## العوائق المفتوحة

- المواضع الدقيقة وأرقام المبرهنات/الصفحات لجميع المصادر.
- جدول تطبيعات موحد بين المراجع.
- تحقق ببليوغرافي من الأوراق الأصلية.
- تحديد النتائج التي ستبرهن داخل الفصل وتلك التي ستقتبس.
- مراجعة مستقلة قبل تجميد السجل.
