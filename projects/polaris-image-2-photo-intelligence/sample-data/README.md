# Sample Data

These files are tiny public-safe contract examples.

- `sample_input.json` shows the expected input shape.
- `sample_output.json` shows one valid output shape.
- `phototours_100_properties.json` contains 100 older PhotoTours property
  records with addresses, lightweight property metadata, and remote photo URL
  references.
- `phototours_video_walkthroughs_100_properties.json` contains 100 PhotoTours
  property records with both photo URL references and video walkthrough URL
  references.

The tiny contract examples use `example.com` placeholders intentionally. They
are not real photo assets and should not be treated as an evaluation dataset.
Use `phototours_100_properties.json` when you need realistic tour shape, address
context, room labels, and remote image URLs. Use
`phototours_video_walkthroughs_100_properties.json` when you need video
walkthroughs that must be chaptered and synced back to photos/spaces.

For a serious submission, add your own public-safe image set and document:

- where the images came from
- whether they are public domain, licensed, generated, or self-created
- how to reproduce the download or generation step
- what labels or expected outputs you used for evaluation

The PhotoTours fixture intentionally stores URL references instead of image
files. Do not commit downloaded image copies unless you have explicit permission
and a clear reason.

The included validator can be run with:

```bash
python3 projects/polaris-image-2-photo-intelligence/scripts/validate_output.py \
  --input projects/polaris-image-2-photo-intelligence/sample-data/sample_input.json \
  --output projects/polaris-image-2-photo-intelligence/sample-data/sample_output.json
```
