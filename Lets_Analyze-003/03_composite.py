"""Average runs with same phase encoding axis."""

import os
import numpy as np
import nibabel as nb

NII_NAMES = [
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC00505XX10_ses-146900_rec-SVR_T1w_registered_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01020XX06_ses-72930_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01022XX08_ses-79430_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01034XX12_ses-51730_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01037XX15_ses-77430_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01059BN12_ses-72330_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01069XX14_ses-79730_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01093AN14_ses-75130_rec-SVR_T1w_registered_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01093BN14_ses-75230_rec-SVR_T1w_reg.nii.gz",
     "/Users/faruk/data/video-siham/video/05_apply_registration/sub-CC01104XX07_ses-82830_rec-SVR_T1w_regis_reg.nii.gz",
    ]

OUTDIR = "/Users/faruk/data/video-siham/video/06_composite"

OUT_NAME = "sub-avg.nii.gz"

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
    data += nii_temp.get_fdata()

# Average
data /= nr_inputs

# Save
img = nb.Nifti1Image(data, affine=nii.affine, header=nii.header)
nb.save(img, os.path.join(OUTDIR, "{}".format(OUT_NAME)))

print('Finished.')
