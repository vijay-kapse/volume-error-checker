# import streamlit as st
# import nibabel as nib
# import numpy as np
# import tempfile

# st.title("NIfTI Image Similarity Metrics")
# st.write("This app calculates the Dice coefficient, Jaccard index, and Volume Overlap Error (VOE) between two NIfTI images.")

# # File uploaders
# uploaded_file1 = st.file_uploader("Upload first NIfTI image", type=".nii.gz")
# uploaded_file2 = st.file_uploader("Upload second NIfTI image", type=".nii.gz")

# def calculate_volume_overlap_error(file_path1, file_path2):
#     """Calculates metrics between two NIfTI images."""
#     img1 = nib.load(file_path1)
#     img2 = nib.load(file_path2)

#     data1 = img1.get_fdata() > 0
#     data2 = img2.get_fdata() > 0

#     if data1.shape != data2.shape:
#         raise ValueError("NIfTI images have different dimensions!")

#     intersection = np.logical_and(data1, data2).sum()
#     union = np.logical_or(data1, data2).sum()

#     dice = (2.0 * intersection) / (data1.sum() + data2.sum())
#     jaccard = intersection / union
#     voe = 1 - dice

#     return dice, jaccard, voe

# # Calculate and display metrics if both files are uploaded
# if uploaded_file1 and uploaded_file2:
#     try:
#         # Create temporary files to store uploaded data
#         with tempfile.NamedTemporaryFile(suffix=".nii.gz", delete=False) as temp_file1, \
#              tempfile.NamedTemporaryFile(suffix=".nii.gz", delete=False) as temp_file2:

#             # Write uploaded content to temporary files
#             temp_file1.write(uploaded_file1.read())
#             temp_file2.write(uploaded_file2.read())

#             # Get temporary file paths
#             temp_file_path1 = temp_file1.name
#             temp_file_path2 = temp_file2.name

#             # Now use the temporary file paths for calculation
#             dice, jaccard, voe = calculate_volume_overlap_error(temp_file_path1, temp_file_path2)

#             st.write("**Metrics:**")
#             st.write(f"Dice coefficient: {dice:.4f}")
#             st.write(f"Jaccard index: {jaccard:.4f}")
#             st.write(f"Volume overlap error: {voe:.4f}")

#     except ValueError as e:
#         st.error(e)


import streamlit as st
import nibabel as nib
import numpy as np
import tempfile
import plotly.graph_objects as go

st.title("NIfTI Image Similarity Metrics")
st.write("This app calculates the Dice coefficient, Jaccard index, and Volume Overlap Error (VOE) between two NIfTI images and visualizes their overlap in 3D.")

# File uploaders
uploaded_file1 = st.file_uploader("Upload first NIfTI image", type=".nii.gz")
uploaded_file2 = st.file_uploader("Upload second NIfTI image", type=".nii.gz")

def calculate_volume_overlap_error(file_path1, file_path2):
    """Calculates metrics between two NIfTI images."""
    img1 = nib.load(file_path1)
    img2 = nib.load(file_path2)

    data1 = img1.get_fdata() > 0
    data2 = img2.get_fdata() > 0

    if data1.shape != data2.shape:
        raise ValueError("NIfTI images have different dimensions!")

    intersection = np.logical_and(data1, data2).sum()
    union = np.logical_or(data1, data2).sum()

    dice = (2.0 * intersection) / (data1.sum() + data2.sum())
    jaccard = intersection / union
    voe = 1 - dice

    return dice, jaccard, voe, data1, data2

def visualize_overlap(data1, data2):
    """Visualizes the overlap of two NIfTI images in 3D."""
    x, y, z = np.nonzero(data1)
    fig = go.Figure(data=[
        go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=1, color='blue'), name='Image 1')
    ])

    x, y, z = np.nonzero(data2)
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=1, color='red'), name='Image 2'))

    x, y, z = np.nonzero(np.logical_and(data1, data2))
    fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=1, color='green'), name='Intersection'))

    fig.update_layout(scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ))

    return fig

# Calculate and display metrics if both files are uploaded
if uploaded_file1 and uploaded_file2:
    try:
        # Create temporary files to store uploaded data
        with tempfile.NamedTemporaryFile(suffix=".nii.gz", delete=False) as temp_file1, \
             tempfile.NamedTemporaryFile(suffix=".nii.gz", delete=False) as temp_file2:

            # Write uploaded content to temporary files
            temp_file1.write(uploaded_file1.read())
            temp_file2.write(uploaded_file2.read())

            # Get temporary file paths
            temp_file_path1 = temp_file1.name
            temp_file_path2 = temp_file2.name

            # Now use the temporary file paths for calculation
            dice, jaccard, voe, data1, data2 = calculate_volume_overlap_error(temp_file_path1, temp_file_path2)

            st.write("**Metrics:**")
            st.write(f"Dice coefficient: {dice:.4f}")
            st.write(f"Jaccard index: {jaccard:.4f}")
            st.write(f"Volume overlap error: {voe:.4f}")

            fig = visualize_overlap(data1, data2)
            st.plotly_chart(fig)

    except ValueError as e:
        st.error(e)
