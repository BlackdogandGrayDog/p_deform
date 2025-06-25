import numpy as np

# Path to your dynamic-shape .npz file
file_path = "simulator_data/trajectory_1/trj_1_ts_99/dataset_tensor.npz"

# Load with pickle allowed for object arrays
data = np.load(file_path, allow_pickle=True)

# Print all keys
print("✅ Keys in file:")
print(data.files)

# Print summary info for each key
for key in data.files:
    print(f"\n🔹 Key: {key}")
    array_list = data[key]  # object array of per-frame tensors
    print(f"  Type: {type(array_list)}, shape: {array_list.shape}, dtype: {array_list.dtype}")

    # # Print shape of each element (i.e., per-frame tensor)
    # for i, arr in enumerate(array_list):
    #     print(f"    Frame {i:02d}: shape = {arr.shape}, dtype = {arr.dtype}")
