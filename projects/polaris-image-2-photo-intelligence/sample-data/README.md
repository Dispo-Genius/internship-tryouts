# Sample Data

These files are tiny public-safe contract examples.

- `sample_input.json` shows the expected input shape.
- `sample_output.json` shows one valid output shape.

The URLs use `example.com` placeholders intentionally. They are not real photo
assets and should not be treated as an evaluation dataset.

For a serious submission, add your own public-safe image set and document:

- where the images came from
- whether they are public domain, licensed, generated, or self-created
- how to reproduce the download or generation step
- what labels or expected outputs you used for evaluation

The included validator can be run with:

```bash
python3 projects/polaris-image-2-photo-intelligence/scripts/validate_output.py \
  --input projects/polaris-image-2-photo-intelligence/sample-data/sample_input.json \
  --output projects/polaris-image-2-photo-intelligence/sample-data/sample_output.json
```
