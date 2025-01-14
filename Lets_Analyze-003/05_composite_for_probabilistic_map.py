"""Average runs with same phase encoding axis."""

import os
import numpy as np
import nibabel as nb

NII_NAMES = [
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC00505XX10_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01020XX06_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01022XX08_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01034XX12_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01037XX15_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01059BN12_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01069XX14_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01093AN14_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01093BN14_seg_refT1_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/07_apply_registration_to_ROIs/CC01104XX07_seg_refT1_reg.nii.gz",
    ]

OUTDIR = "/Users/faruk/data/video-siham/video/08_composite_probabilistic_map"

OUT_NAME = "sub-avg_probabilistic_map.nii.gz"

# =============================================================================
# Output directory
if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)
print("  Output directory: {}".format(OUTDIR))

# =============================================================================
# Load first image
nii = nb.load(NII_NAMES[0])
data = np.zeros(nii.shape)

# Add all images
nr_inputs = len(NII_NAMES)
for i in range(nr_inputs):
    nii_temp = nb.load(NII_NAMES[i])
    temp = np.asarray(nii_temp.dataobj) > 0
    data = data + temp

# Average
data /= nr_inputs

# Save
img = nb.Nifti1Image(data, affine=nii.affine, header=nii.header)
nb.save(img, os.path.join(OUTDIR, "{}".format(OUT_NAME)))

print('Finished.')
