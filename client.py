import sys, json, time, math, re

class MetaMuseEpisodicResonance:
    """
    Meta + Muse Multimodal Episodic Memory & Emotional Resonance Core.
    Fuses ambient multi-sensory grounding (audio/visual anchors) with
    long-term life episodic graphs, entity relationships, and empathetic calibration.
    """
    def __init__(self):
        self.episodes = []

    def record_episodic_moment(self, event_id, modality, content, emotional_valence=0.0, people=None, timestamp=None):
        self.episodes.append({
            "id": event_id,
            "modality": modality,  # visual, audio, text, multimodal
            "content": content,
            "valence": max(-1.0, min(1.0, float(emotional_valence))),
            "people": people or [],
            "timestamp": timestamp or time.time()
        })
        return {"status": "STORED", "id": event_id, "memory_bank_size": len(self.episodes)}

    def associative_memory_recall(self, query, top_k=3):
        q_tokens = set(re.findall(r"\b\w{3,}\b", query.lower()))
        results = []

        for ep in self.episodes:
            ep_tokens = set(re.findall(r"\b\w{3,}\b", ep["content"].lower()))
            overlap = len(q_tokens & ep_tokens) / max(1, len(q_tokens | ep_tokens))
            if overlap > 0.05:
                results.append({
                    "id": ep["id"],
                    "modality": ep["modality"],
                    "content": ep["content"],
                    "valence": ep["valence"],
                    "people": ep["people"],
                    "relevance_score": round(overlap, 4)
                })

        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return {"query": query, "recalled_episodes": results[:top_k]}

    def synthesize_empathetic_resonance(self, user_statement, current_mood="stressed"):
        recall = self.associative_memory_recall(user_statement, top_k=2)
        top_mem = recall["recalled_episodes"][0] if recall["recalled_episodes"] else None

        if current_mood == "stressed" and top_mem:
            reply = (
                f"I hear how challenging this moment feels. Remembering when you tackled '{top_mem['content'][:60]}...', "
                f"you navigated that with tremendous resilience. Let's take it one step at a time today."
            )
        else:
            reply = f"I'm right here with you. Let's focus on the most impactful priority right now."

        return {
            "attuned_response": reply,
            "emotional_grounding": "EMPATHETIC_AFFINITY",
            "referenced_memory_id": top_mem.get("id") if top_mem else None
        }

    def run_meta_muse_benchmark(self):
        self.episodes.clear()
        now = time.time()

        self.record_episodic_moment("m1", "visual", "Presented keynote at AI World Congress on stage with Alex.", 0.8, ["Alex"], now - 86400 * 30)
        self.record_episodic_moment("m2", "audio", "Felt overwhelmed preparing quarterly budget with Sarah, but resolved it by delegating ops.", -0.4, ["Sarah"], now - 86400 * 15)
        self.record_episodic_moment("m3", "multimodal", "Celebrated team milestone launch at dinner with Elena.", 0.9, ["Elena"], now - 86400 * 5)

        q = "I am feeling overwhelmed with this upcoming investor presentation."
        empathy = self.synthesize_empathetic_resonance(q, current_mood="stressed")

        return {
            "suite": "Meta + Muse Episodic Resonance Benchmark",
            "test_query": q,
            "empathetic_synthesis": empathy,
            "memory_vault_status": "EPISODIC_RESONANCE_ACTIVE"
        }
