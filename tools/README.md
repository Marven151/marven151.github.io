# Page generator

The two pages (Polish and English) are generated from `strings.py` (all texts) and `build.py` (markup, styles, script). The output is plain static HTML.

```bash
cd tools
python3 build.py
```

The script reads Lighthouse results from `../lhx/*.json` if they exist, which is why the build step is not part of the published site.
