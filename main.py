import time
from agents import DataIngestionAgent, AnalystAgent, SynthesisAgent

def run_market_analysis_pipeline():
    print("=== FinSight Market Analysis Pipeline Starting ===")
    
    ingestor = DataIngestionAgent()
    analyst = AnalystAgent()
    editor = SynthesisAgent()

    # Step 1: Massive context ingestion
    raw_data = ingestor.process_large_docs(docs_count=40)
    time.sleep(1)

    # Step 2: Multi-turn reasoning (The Token Eater)
    verified_insights = analyst.cross_verify(raw_data, turns=5)
    time.sleep(1)

    # Step 3: Synthesis
    final_report = editor.generate_final_report(verified_insights)
    
    print("=== Pipeline Complete. High-Token Task Successfully Processed. ===")

if __name__ == "__main__":
    run_market_analysis_pipeline()
