const { test } = require('node:test');
const assert = require('node:assert/strict');
const { execFileSync } = require('node:child_process');
const path = require('node:path');

test('rejects hallucinated word times outside the audio and preserves unknown words', () => {
  const script = `
import json, sys
sys.path.insert(0, ${JSON.stringify(path.resolve(__dirname, '../skills/onbeat/scripts'))})
from word_times import valid_words
words = [
 dict(text='Romi', start=1.0, end=1.5),
 dict(text='Thank', start=14.85, end=20.019),
 dict(text='you', start=21.053, end=43.796),
 dict(text='unknown', start=2.0, end=None),
 dict(text='nan', start=float('nan'), end=3.0),
 dict(text='backwards', start=4.0, end=3.0),
]
usable, rejected = valid_words(words, 15.4490625)
print(json.dumps(dict(usable=usable, rejected=[w['text'] for w in rejected])))
`;
  const result = JSON.parse(execFileSync('python3', ['-c', script], { encoding: 'utf8' }));
  assert.deepEqual(result.usable, [
    { text: 'Romi', start: 1, end: 1.5 },
    { text: 'unknown', start: null, end: null },
  ]);
  assert.deepEqual(result.rejected, ['Thank', 'you', 'nan', 'backwards']);
});
