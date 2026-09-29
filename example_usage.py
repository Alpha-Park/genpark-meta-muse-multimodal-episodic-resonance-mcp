from client import MetaMuseEpisodicResonance
import json

muse = MetaMuseEpisodicResonance()
print("=== META + MUSE EPISODIC RESONANCE BENCHMARK ===")
res = muse.run_meta_muse_benchmark()
print(json.dumps(res, indent=2))
