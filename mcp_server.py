import sys, json
from client import MetaMuseEpisodicResonance

def handle_mcp():
    muse = MetaMuseEpisodicResonance()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(muse.run_meta_muse_benchmark(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            
            if method == "initialize":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {"name": "genpark-meta-muse-multimodal-episodic-resonance-mcp", "version": "1.0.0"},
                    "capabilities": {"tools": {}}
                }}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [
                    {"name": "record_episodic_moment", "description": "Store multimodal episodic moment.", "inputSchema": {"type": "object", "properties": {"event_id": {"type": "string"}, "content": {"type": "string"}}}},
                    {"name": "associative_memory_recall", "description": "Recall memories based on association.", "inputSchema": {"type": "object", "properties": {"query": {"type": "string"}}}},
                    {"name": "synthesize_empathetic_resonance", "description": "Formulate emotionally attuned response.", "inputSchema": {"type": "object", "properties": {"user_statement": {"type": "string"}}}},
                    {"name": "run_meta_muse_benchmark", "description": "Run Meta + Muse benchmark.", "inputSchema": {"type": "object"}}
                ]}}
            elif method == "tools/call":
                tname = req.get("params", {}).get("name")
                args = req.get("params", {}).get("arguments", {})
                if tname == "record_episodic_moment":
                    res = muse.record_episodic_moment(args.get("event_id", "m"), args.get("modality", "text"), args.get("content", ""))
                elif tname == "associative_memory_recall":
                    res = muse.associative_memory_recall(args.get("query", ""))
                elif tname == "synthesize_empathetic_resonance":
                    res = muse.synthesize_empathetic_resonance(args.get("user_statement", ""))
                else:
                    res = muse.run_meta_muse_benchmark()
                resp = {"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
            else:
                resp = {"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}
            
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_mcp()
