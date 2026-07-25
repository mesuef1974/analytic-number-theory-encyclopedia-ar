# تدقيق Consensus الأدبي للفصل الثامن عشر

التاريخ: 2026-07-25

## الهدف

استخدام Consensus لتثبيت موقع الفصل الثامن عشر داخل الأدبيات الأكاديمية الحديثة والكلاسيكية، مع التركيز على:

1. اختبارات مشتقات فان دير كوربوت.
2. عملية `B` وصياغة التحويل الأساسية.
3. عمليتي `A` و`B` ونظرية الأزواج الأسية.
4. حدود الادعاء وعدم نسبة التحسينات الحديثة إلى متن موسوعي تمهيدي.

## نتائج البحث

### 1. المرجع البنيوي الرئيس

- S. Graham وG. Kolesnik، *Van der Corput's Method of Exponential Sums* (1991).
- يغطي الكتاب: أبسط تقديرات فان دير كوربوت، نظرية الأزواج الأسية، التطبيقات، وحساب الأزواج المثلى.
- القرار: مرجع رئيس لهيكل الفصل، لكن الصياغات التي ستثبت داخليًا يجب أن تراجع أيضًا في Montgomery--Vaughan أو مصدر أولي مناسب.

### 2. اختبارات المشتقات العليا

- O. Robert، “On van der Corput’s k-th derivative test for exponential sums”، *Indagationes Mathematicae* 27 (2016), 559--589.
- يقدم نظرة على اختبار المشتقة من الرتبة `k`، أمثلية بعض التقديرات، وتحسينات أحدث.
- القرار: يستخدم لتثبيت أن نظرية المشتقات العليا أوسع من نطاق الفصل؛ لا ندعي أفضل صيغة حديثة.

### 3. عملية B والتحسينات الحديثة

- Hong-quan Liu، “On van der Corput's method for exponential sums” (2018).
- يدرس حد الخطأ في عملية `B` ويوسع فئات المجاميع التي تعالج بأزواج ناتجة عن تكرار عمليتي `A` و`B`.
- القرار: عملية `B` الكاملة وصيغ خطئها الدقيقة تصنف `CITED` ما لم يثبت الفصل نسخة محدودة بوضوح.

### 4. النتيجة التحويلية الأساسية

- Hong-quan Liu، “On a fundamental result in van der Corput's method of estimating exponential sums”، *Acta Arithmetica* 90 (1999), 357--370.
- يعالج الإجراء التحويلي الأساسي عندما تكون المشتقة الثانية مستمرة ولا تغير إشارتها.
- القرار: يدعم وجوب تجميد شروط النعومة، الرتابة/الإشارة، ومجال الطور قبل صياغة عملية `B`.

## الاستنتاجات الحاكمة

```text
FIRST-DERIVATIVE-TEST = MUST USE DISTANCE-TO-INTEGERS OR AN EQUIVALENT PRECISE FORM
SECOND-DERIVATIVE-TEST = CLASSICAL BOUNDED VERSION MAY BE PROVED-HERE
A-PROCESS = VAN-DER-CORPUT DIFFERENCING / PROVED-HERE CANDIDATE
B-PROCESS = LIMITED VERSION OR CITED
EXPONENT-PAIR-THEORY = CITED / EXPLAINED, NOT FULLY PROVED-HERE
HIGHER-DERIVATIVE-TESTS = DEFERRED / CONTEXT ONLY
BEST-MODERN-BOUNDS = OUT OF SCOPE
```

## أثر التدقيق على بوابة التأليف

- سجل الأدلة وخريطة البرهان موجودان.
- لم تغلق البوابة بعد.
- البنود الحاجزة المتبقية:
  1. تثبيت نص دقيق لاختبار المشتقة الأولى.
  2. تثبيت نص دقيق لاختبار المشتقة الثانية.
  3. حسم النسخة المحدودة من عملية `B`.
  4. تدقيق عدم الدور مع الفصل 17.
  5. مراجعة مستقلة قبل `PASS-FOR-AUTHORING`.

## روابط Consensus

- https://consensus.app/papers/van-der-corputs-method-of-exponential-sums-graham-kolesnik/cb3625055dc0566c914d1753e9425118/
- https://consensus.app/papers/on-van-der-corputs-kth-derivative-test-for-exponential-sums-robert/fd85eedf97c055768660c563d5820ba7/
- https://consensus.app/papers/on-van-der-corputs-method-for-exponential-sums-liu/25e223090ce65815a496dc06c7319242/
- https://consensus.app/papers/on-a-fundamental-result-in-van-der-corputs-method-of-liu/5bf97dab02a35a7a9808cf7fee28972c/

## الحكم

```text
CONSENSUS-LITERATURE-AUDIT = PASS-AS-SCOPING-INPUT
PRE-AUTHORING-GATE         = OPEN
PASS-FOR-AUTHORING         = NO
AUTHORING                  = BLOCKED
```
