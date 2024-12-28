import os
import nibabel as nib
import matplotlib.pyplot as plt

# Ruta al directorio FreeSurfer
freesurfer_dir = "/home/rmbk/Documents"

# Especifica el sujeto que quieres visualizar
subject = "OAS30001_MR_d2430"

# Ruta al archivo anatómico del sujeto
anat_file = os.path.join(freesurfer_dir, subject, "mri", "T1.mgz")

# Verificar si el archivo existe
if not os.path.exists(anat_file):
    print(f"Archivo no encontrado: {anat_file}")
else:
    print(f"Procesando: {anat_file}")
    
    # Cargar el volumen
    try:
        anat_img = nib.load(anat_file)
        anat_data = anat_img.get_fdata()

        # Seleccionar el índice para el "corte axial" (más arriba en el cerebro)
        axial_index = anat_data.shape[1] // 2 + 19
          # Mueve el corte 10 slices más arriba
        
        # Verifica que el índice esté dentro del rango válido
        if 0 <= axial_index < anat_data.shape[1]:
            # Extraer el "corte axial" (realmente un corte coronal por la orientación)
            axial_slice = anat_data[:, axial_index, :]

            # Visualizar el corte axial
            plt.imshow(axial_slice.T, cmap="gray", origin="lower")  # Transpuesta para orientación correcta
            plt.title(f"Corte axial ajustado más arriba - {subject}")
            plt.axis("off")

            # Guardar el gráfico como imagen
            output_file = f"{subject}_brain_axial_slice_higher.png"
            plt.savefig(output_file)  # Guardar la imagen
            print(f"Gráfico guardado como {output_file}")

            # Mostrar el gráfico
            plt.show()
        else:
            print("Índice fuera de rango. Ajusta el valor de axial_index.")
    except Exception as e:
        print(f"Error al procesar {anat_file}: {e}")


