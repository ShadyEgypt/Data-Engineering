

def load_data(data_to_load, target_dir):
    try:
        data_to_load.to_csv(target_dir, index=False)
        return(f"Saved in: {target_dir}")

    except Exception as exp:
        return(f"Error in load_data: {exp}")
