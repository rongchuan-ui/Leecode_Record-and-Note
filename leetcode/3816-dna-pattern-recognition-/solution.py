import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples["has_start"]=samples["dna_sequence"].str.startswith("ATG").astype(int)
    samples["has_stop"]=samples["dna_sequence"].str.endswith(("TAA","TAG","TGA")).astype(int)
    samples["has_atat"]=samples["dna_sequence"].str.contains("ATAT").astype(int)
    samples["has_ggg"]=(samples["dna_sequence"].str.contains("GGGG") |samples["dna_sequence"].str.contains("GGG")) .astype(int)
    return samples.sort_values("sample_id")
    

    # # 1. Extract the sequence column to minimize repeated DataFrame access
    # seq = samples["dna_sequence"]
    # # 2. Use assign() to inject all new columns at once (more memory efficient)
    # # 3. Use regex=False for simple substring matching to improve performance
    # samples = samples.assign(
    #     # Check if sequence starts with ATG
    #     has_start=seq.str.startswith("ATG").astype('int8'),
    #     # Check if sequence ends with TAA, TAG, or TGA
    #     has_stop=seq.str.endswith(("TAA", "TAG", "TGA")).astype('int8'),
    #     # Check if sequence contains the motif ATAT
    #     has_atat=seq.str.contains("ATAT", regex=False).astype('int8'),
    #     # Check if sequence contains at least 3 consecutive Gs (GGG)
    #     # Note: If it contains GGGG, it automatically contains GGG, so one check is enough.
    #     has_ggg=seq.str.contains("GGG", regex=False).astype('int8')
    # )
    # # 4. Sort results by sample_id in ascending order
    # return samples.sort_values("sample_id")
