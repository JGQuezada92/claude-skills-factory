# Skill Packaging - Zip File Locations

## Where Zip Files Are Created

### Default Location (When No `--output` Specified)

When you run `package_skill.py` without specifying an `--output` path, the zip file is created **inside the skill folder itself**:

```
skill-factory/
└── generated_skills/
    └── global-market-liquidity-analyst/
        ├── SKILL.md
        ├── scripts/
        ├── references/
        ├── assets/
        └── global-market-liquidity-analyst.zip  ← ZIP FILE IS HERE
```

**Full Path:**
```
C:\Users\jquez\Cursor Applications\skills-factory-main-folder\skill-factory\generated_skills\global-market-liquidity-analyst\global-market-liquidity-analyst.zip
```

### Code Reference

The packaging logic is in `package_skill.py`, lines 134-138:

```python
# Determine output_path
if output_path is None:
    output_path = self.skill_path / f"{self.skill_name}.zip"
else:
    output_path = Path(output_path)
```

This means:
- `self.skill_path` = the skill folder path (e.g., `generated_skills/global-market-liquidity-analyst`)
- `self.skill_name` = the folder name (e.g., `global-market-liquidity-analyst`)
- Result: `{skill_folder}/{skill_name}.zip`

## How to Package a Skill

### Basic Usage (Creates zip in skill folder)
```bash
python package_skill.py generated_skills\global-market-liquidity-analyst
```

### Custom Output Location
```bash
python package_skill.py generated_skills\global-market-liquidity-analyst --output "C:\Users\jquez\Desktop\my-skill.zip"
```

### Skip Validation (Faster)
```bash
python package_skill.py generated_skills\global-market-liquidity-analyst --no-validate
```

### Batch Package All Skills
```bash
python package_skill.py --batch generated_skills
```

## What Gets Included in the Zip

The zip file includes (from `_create_zip` method, lines 174-204):

1. **SKILL.md** - Required at root level
2. **scripts/** - All Python scripts and files
3. **references/** - Reference documentation
4. **assets/** - Asset files (images, etc.)
5. **LICENSE.txt** - If present
6. **manifest.json** - Auto-generated with file checksums

### Excluded from Zip

- TESTING_GUIDE/ directory
- *.zip files
- Hidden files (.*)
- __pycache__/
- *.pyc, *.pyo files
- test_*.py files
- .git/ directory

## Current Zip File Status

✅ **Zip file exists:**
- Location: `skill-factory\generated_skills\global-market-liquidity-analyst\global-market-liquidity-analyst.zip`
- Size: ~23 KB
- Ready to upload to Claude!

## To Upload to Claude

1. Navigate to: `skill-factory\generated_skills\global-market-liquidity-analyst\`
2. Find: `global-market-liquidity-analyst.zip`
3. Upload this zip file to Claude.ai when adding a new skill

## Summary

The zip file is created **inside the skill folder**, not in the parent `skill-factory` directory. This keeps the packaged skill with its source files for easy management.

