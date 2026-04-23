import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # tree_new=tree.merge(
    #     tree, 
    #     left_on="id",
    #     right_on="p_id",
    #     how="left",
    #     suffixes=("_parent","_child")
    # )
    # tree_new["type"]=(tree_new.apply(
    #     lambda x: "Root" if pd.isna(x["p_id_parent"]) 
    #                 else("Inner" if pd.notna(x["id_child"]) else "Leaf"),
    #     axis=1
    #     )
    # )
    # tree_new =tree_new.drop_duplicates("id_parent").rename(columns={
    #     "id_parent":"id",
    # })
    # return tree_new[["id","type"]]

    parents = set(tree['p_id'].dropna())
    
    tree['type'] = 'Leaf'

    tree.loc[tree['id'].isin(parents), 'type'] = 'Inner'
    
    tree.loc[tree['p_id'].isna(), 'type'] = 'Root'
    
    return tree[['id', 'type']]
