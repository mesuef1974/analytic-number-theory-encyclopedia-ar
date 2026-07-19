from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Expected exactly one match in {path}, found {count}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


batch2 = "volumes/volume-01-foundations/chapters/chapter-07-dirichlet-l-functions-batch-02.tex"
batch4 = "volumes/volume-01-foundations/chapters/chapter-07-dirichlet-l-functions-batch-04.tex"
batch5 = "volumes/volume-01-foundations/chapters/chapter-07-dirichlet-l-functions-batch-05.tex"

replace_once(batch2, "هذه الت合同 متوافقة", "وهذه التوافقات متّسقة")

old_fe = r"""تتناقص \(\theta_\chi(t)\) أسيًا عندما \(t\to\infty\). ويحول تحويل
ثيتا سلوكها عند \(t\to0^+\) إلى سلوك
\(\theta_{\overline\chi}(1/t)\) عند اللانهاية، ولذلك يتقارب التكامل
محليًا بانتظام لكل \(s\in\mathbb C\)، ويعرف دالة تامة.

وباستخدام تحويل ثيتا ثم تغيير المتغير \(u=1/t\):
\begin{align*}
\Lambda(s,\chi)
&=
\frac{\varepsilon_\chi}{2}
\int_0^\infty
\theta_{\overline\chi}(1/t)
 t^{(s-a-1)/2}\,\frac{dt}{t}\\
&=
\frac{\varepsilon_\chi}{2}
\int_0^\infty
\theta_{\overline\chi}(u)
 u^{(1-s+a)/2}\,\frac{du}{u}\\
&=
\varepsilon_\chi\Lambda(1-s,\overline\chi).
\end{align*}"""

new_fe = r"""نقسم التكامل عند \(t=1\). وفي الجزء \(0<t<1\) نستعمل تحويل
ثيتا ثم نغيّر المتغير \(u=1/t\)، فنحصل على
\begin{align*}
\Lambda(s,\chi)
&=
\frac12\int_1^\infty
\theta_\chi(t)t^{(s+a)/2}\,\frac{dt}{t}\\
&\quad+
\frac{\varepsilon_\chi}{2}\int_1^\infty
\theta_{\overline\chi}(u)u^{(1-s+a)/2}\,\frac{du}{u}.
\end{align*}
يتقارب التكاملان محليًا بانتظام لكل \(s\in\mathbb C\)، بسبب التناقص
الأسي لدالتي ثيتا عند اللانهاية، ولذلك تمثل الصيغة دالة تامة.

وبتطبيق الصيغة نفسها على \(\Lambda(1-s,\overline\chi)\)، ثم استعمال
\[
\varepsilon_\chi\varepsilon_{\overline\chi}
=
\frac{\tau(\chi)\tau(\overline\chi)}{i^{2a}q}
=
\frac{\chi(-1)q}{(-1)^a q}
=1,
\]
نجد أن الحدين يتبادلان، ومن ثم
\[
\Lambda(s,\chi)
=
\varepsilon_\chi\Lambda(1-s,\overline\chi).
\]"""
replace_once(batch2, old_fe, new_fe)

old_corollary = r"""\begin{corollary}
إذا كانت \(\chi\) غير حقيقية، فإن الصفر البديهي عند \(s=0\) في الحالة
الزوجية بسيط، لأن المعادلة الوظيفية تربطه بقيمة
\(L(1,\overline\chi)\ne0\).
\end{corollary}"""

new_remark = r"""\begin{remark}[بساطة الصفر عند الصفر في الحالة غير الحقيقية]
إذا كانت \(\chi\) غير حقيقية وزوجية، فإن الصفر البديهي عند \(s=0\)
بسيط، لأن المعادلة الوظيفية تربطه بقيمة
\(L(1,\overline\chi)\ne0\). وهذه حالة خاصة من النتيجة العامة
\ref{cor:dirichlet-l-trivial-zeros}، وليست نتيجة مستقلة تحتاج إلى معرّف
إضافي.
\end{remark}"""
replace_once(batch4, old_corollary, new_remark)

old_eta = r"""ثبت عددًا حقيقيًا \(c>\sigma_0\). لكل \(k\geq0\) واختر
\(\eta>0\) بحيث \(c-\eta>\sigma_0\). لدينا التقدير القياسي"""

new_eta = r"""ثبت عددًا حقيقيًا \(c>\sigma_0\)، ثم ثبت عددًا
\(\eta>0\) بحيث \(c-\eta>\sigma_0\). عندئذ، لكل \(k\geq0\)، لدينا
التقدير القياسي"""
replace_once(batch5, old_eta, new_eta)

changelog = Path("CHANGELOG.md")
text = changelog.read_text(encoding="utf-8")
change_marker = "### تغيّر\n"
change_bullet = (
    "- تطبيق تصحيحات المراجعة الخارجية الآلية للفصل السابع: إزالة محرفي "
    "CJK المتسربين، وتقسيم تكامل ميلين عند \\(t=1\\)، وتثبيت اختيار "
    "\\(\\eta\\) في مبدأ لاندو، وتحويل نتيجة مكررة إلى ملاحظة تحيل "
    "إلى `ANT-COR-07-05`.\n"
)
if change_bullet not in text:
    if change_marker not in text:
        raise SystemExit("CHANGELOG marker not found")
    changelog.write_text(
        text.replace(change_marker, change_marker + change_bullet, 1),
        encoding="utf-8",
    )

progress = Path("docs/PROGRESS.md")
text = progress.read_text(encoding="utf-8")
progress_marker = "- إغلاق النتيجة العامة `ANT-THM-07-09` بحالة `PROVED-HERE`.\n"
progress_bullet = (
    "- إغلاق تصحيحات المراجعة الخارجية الآلية وإزالة المحارف غير العربية "
    "من مصدر الفصل.\n"
)
if progress_bullet not in text:
    if progress_marker not in text:
        raise SystemExit("PROGRESS marker not found")
    text = text.replace(progress_marker, progress_marker + progress_bullet, 1)
text = text.replace(
    "- تدقيق مستقل كامل للصيغ وعوامل غاما وجذور العدد.\n",
    "- المراجعة البشرية المستقلة النهائية للصيغ وعوامل غاما وجذور العدد.\n",
    1,
)
progress.write_text(text, encoding="utf-8")

report = Path("docs/CHAPTER_07_EXTERNAL_AI_REVIEW_CORRECTIONS_2026-07-19.md")
report.write_text(
    r"""# إغلاق تصحيحات المراجعة الخارجية الآلية للفصل السابع

التاريخ: 2026-07-19

الحالة: `PASS-WITH-MINOR-CORRECTIONS / CORRECTIONS-CLOSED`

## التصحيحات المنفذة

1. إزالة المحرفين الصينيين `合同` واستبدالهما بصياغة عربية سليمة.
2. تقسيم تكامل ميلين عند \(t=1\) في برهان المعادلة الوظيفية.
3. تثبيت \(\eta\) قبل استعمال التقدير اللوغاريتمي في مبدأ لاندو.
4. تحويل النتيجة المكررة عن بساطة الصفر عند \(s=0\) إلى ملاحظة تحيل إلى
   `ANT-COR-07-05`.
5. تحديث سجل التغييرات ولوحة التقدم.

لا تعد هذه مراجعة بشرية مستقلة؛ لذلك تبقى حالة الفصل `DRAFT`.
""",
    encoding="utf-8",
)

offenders = []
chapter_dir = Path("volumes/volume-01-foundations/chapters")
for source in chapter_dir.glob("chapter-07*.tex"):
    for index, character in enumerate(source.read_text(encoding="utf-8")):
        if "\u4e00" <= character <= "\u9fff":
            offenders.append((str(source), index, character))
if offenders:
    raise SystemExit(f"CJK characters remain: {offenders}")

print("Chapter 7 review corrections applied successfully.")
