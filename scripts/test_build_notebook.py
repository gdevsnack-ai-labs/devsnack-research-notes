import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_notebook import build_notebook, collect_notes, parse_frontmatter

ROOT = Path(__file__).resolve().parents[1]


class BuildNotebookTest(unittest.TestCase):
    def test_frontmatter_contains_two_dates_and_status(self):
        source = ROOT / 'source' / 'agents' / 'oh-my-hermes-omh.md'
        meta, body = parse_frontmatter(source.read_text())
        self.assertEqual(meta['researched_date'], '2026-08-19')
        self.assertEqual(meta['published_date'], '2026-08-30')
        self.assertEqual(meta['status'], 'experiment-candidate')
        self.assertIn('## 확인한 내용', body)
        self.assertIn('## 확인하지 못한 내용', body)

    def test_real_source_inventory_is_24_notes(self):
        notes = collect_notes(ROOT / 'source')
        self.assertEqual(len(notes), 24)
        self.assertEqual(sum(note['category'] == 'agents' for note in notes), 5)
        self.assertEqual(sum(note['category'] == 'models' for note in notes), 6)
        self.assertEqual(sum(note['category'] == 'media' for note in notes), 9)
        self.assertEqual(sum(note['category'] == 'tools' for note in notes), 4)
        self.assertTrue(all(note['promoted_asset_url'] is None for note in notes))

    def test_build_writes_manifest_index_and_generated_html(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / 'source', root / 'source')
            build_notebook(root)
            manifest = json.loads((root / 'data' / 'research-notes.json').read_text())
            self.assertEqual(len(manifest), 24)
            self.assertTrue((root / 'index.html').exists())
            self.assertEqual(len(list((root / 'notes').glob('*.html'))), 24)
            generated = (root / 'notes' / 'oh-my-hermes-omh.html').read_text()
            self.assertIn('../assets/notebook.css', generated)
            self.assertIn('<h1>', generated)
            self.assertIn('class="meta-card"', generated)
            self.assertIn('status-chip', generated)
            self.assertIn('https://devsnack-blog.vercel.app/research/oh-my-hermes-omh-hermes-agent', generated)


if __name__ == '__main__':
    unittest.main()
