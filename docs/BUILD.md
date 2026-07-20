# بناء الموسوعة بصيغة PDF

## المخرج المحلي

بعد نجاح البناء، تُنشأ الملفات:

```text
build/main.pdf
releases/preview.pdf
releases/preview.pdf.sha256
```

نسخة `releases/preview.pdf` مخصصة للمعاينة المحلية. أما ملفات PDF الرسمية ذات أرقام الإصدارات فتنشر عبر GitHub Releases.

## المتطلبات على Windows

يجب تثبيت توزيعة LaTeX تحتوي على:

- XeLaTeX
- Biber
- Polyglossia
- BibLaTeX
- خط Amiri للنص العربي
- خط Latin Modern Roman للنص اللاتيني

يمكن استخدام MiKTeX أو TeX Live. لا يحتاج البناء المحلي إلى Perl أو Latexmk. بعد التثبيت، افتح PowerShell جديدًا وتحقق:

```powershell
xelatex --version
biber --version
```

## البناء بأمر واحد

من جذر المستودع:

```powershell
cd "D:\analytic-number-theory-encyclopedia-ar"
.\scripts\build.ps1 -Clean -Open
```

- `-Clean`: يحذف ملفات البناء القديمة.
- `-Open`: يفتح PDF بعد نجاح البناء.

للبناء دون فتح الملف:

```powershell
.\scripts\build.ps1
```

## المزامنة والبناء وإصدار إيصال

لتجنب البناء من فرع أو رأس قديم، استخدم المسار المتزامن:

```powershell
cd "D:\analytic-number-theory-encyclopedia-ar"
.\scripts\sync-build.ps1 -Open
```

ينفذ السكربت بالترتيب:

1. يرفض العمل إذا كانت شجرة Git غير نظيفة.
2. ينفذ `git fetch --prune origin`.
3. ينتقل إلى فرع الفصل الثاني عشر.
4. ينفذ `git pull --ff-only` لمنع الدمج المحلي العرضي.
5. يتحقق من تطابق `HEAD` المحلي مع `origin/<branch>`.
6. يشغّل `scripts/build.ps1 -Clean`.
7. يحسب SHA256 وحجم PDF وعدد الصفحات عندما تتوفر `pdfinfo` أو `mutool` أو Python مع `pypdf`.
8. ينشئ `docs/LOCAL_BUILD_RECEIPT.md` من النتائج الفعلية.

لتسجيل الإيصال في Git ودفعه إلى الفرع نفسه:

```powershell
.\scripts\sync-build.ps1 -Open -CommitReceipt -Push
```

لا تستعمل `-Push` من دون `-CommitReceipt`. ولا يجعل نجاح البناء المحلي الفصل `REVIEWED` أو `RELEASE-READY` تلقائيًا.

## تنظيف الملفات

```powershell
.\scripts\clean.ps1
```

ولحذف نسخة المعاينة أيضًا:

```powershell
.\scripts\clean.ps1 -IncludePreview
```

## البناء التلقائي على GitHub

بعد كل Push يؤثر في ملفات الكتاب، يشغّل GitHub Actions workflow باسم:

```text
Build encyclopedia PDF
```

عند نجاحه:

1. افتح صفحة المستودع على GitHub.
2. افتح تبويب **Actions**.
3. اختر آخر تشغيل ناجح.
4. في قسم **Artifacts** نزّل:
   `analytic-number-theory-encyclopedia-preview`.

ملف Artifact مؤقت للمعاينة، وليس إصدارًا رسميًا.

## التحقق المحلي من Artifact

يمكن تنزيل Artifact إلى بيئة أخرى وفحص ملف PDF محليًا. يجب التمييز بين:

- `SOURCE-BUILD`: بناء PDF من ملفات المصدر المحلية بعد مزامنة Git.
- `ARTIFACT-VERIFICATION`: فتح وفحص PDF الذي بناه GitHub Actions بعد تنزيله.

يسجل التحقق المنفذ للفصل الثاني عشر في:

```text
docs/LOCAL_ARTIFACT_VERIFICATION_2026-07-20.md
```

ولا يجوز تحويل تحقق Artifact إلى ادعاء بناء مصدر محلي.

## التحقق العددي المسجل

لتشغيل تجربة ANT-COMP-06-01 من جذر المستودع بعد إعداد بيئة Python:

```text
python -m pip install -r computational/python/requirements-zeta.txt
python computational/python/hardy_z_low_zeros.py --config computational/python/config/hardy_z_first10.json
```

يشغّل GitHub Actions كذلك workflow باسم:

```text
Zeta numerical validation
```

نجاحه يثبت اجتياز شروط القبول البرمجية المسجلة فقط، ولا يثبت اكتمال
الأصفار ولا يقدم دليلًا على فرضية ريمان. راجع
[سجل التجارب](EXPERIMENTS_REGISTRY.md) وتعليمات
[مختبر Python](../computational/python/README.md).

## إنشاء إصدار رسمي

بعد التأكد من نظافة المستودع ونجاح البناء:

```powershell
.\scripts\release.ps1 -Version "v0.4.0" -Push
```

ينشئ السكربت Tag ويدفعه إلى GitHub. عندها يشغّل workflow باسم:

```text
Publish tagged PDF release
```

ويُنشئ GitHub Release يحتوي على:

- ملف PDF موسوم برقم الإصدار.
- ملف SHA256 للتحقق من سلامة التنزيل.

## معالجة الأخطاء

### الأداة غير موجودة

أغلق PowerShell وافتحه بعد تثبيت MiKTeX أو TeX Live. إذا استمر الخطأ، أضف مجلد الأدوات إلى متغير `PATH`.

### حزمة LaTeX ناقصة

في MiKTeX فعّل تثبيت الحزم الناقصة تلقائيًا، أو ثبّتها من MiKTeX Console.

### فشل Biber

احذف مجلد `build` ثم أعد البناء:

```powershell
.\scripts\build.ps1 -Clean
```

### اختلاف المحلي عن GitHub

قارن سجل البناء المحلي بصفحة Actions. قد تختلف إصدارات TeX Live؛ النسخة المنشورة رسميًا هي ناتج workflow المرتبط بالـTag.
