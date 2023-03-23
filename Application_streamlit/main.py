import streamlit as st
import pickle
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image as k_image
from tensorflow.keras.models import load_model
SEED = 49


def load_pickle(file_name):
    file_path = "./ressources" + f"/{file_name}.pkl"
    file_to_return = open(file_path, 'rb')
    file_to_return = pickle.load(file_to_return)
    return file_to_return


def load_ressources():
    model_ = load_model("./ressources/xception_based_model.h5", compile=False)
    class_names_ = load_pickle("class_names")
    batch_images_ = load_pickle("batch_image")
    batch_labels_ = load_pickle("batch_label")

    return model_, class_names_, batch_images_, batch_labels_


def prepare_image(img):
    img = img.resize((500,500))
    img_tensor = k_image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    return img_tensor


@st.cache_data()
def get_model_predictions(_model, class_names, img):
    """
    Objectif :
        Retournée la prédiction de la race du chien sur l'image en argument
    Arguments:
        img (tf.tensor) : tenseur de forme (500,500,3) ou  (1,500,500,3) représentant une image brute contenant un chien
    Valeur retournée:
        prediction (str) : race prédite par le modèle
    """

    if len(img.shape)==4:
      prediction = class_names[np.argmax(model.predict(img))]
    else:
      prediction = class_names[np.argmax(model.predict(tf.expand_dims(img, axis=0)))]
    return prediction


if __name__ == "__main__":

    model, class_names, batch_images, batch_labels = load_ressources()
    batch_breeds = [class_names[label] for label in batch_labels]
    batch_breeds_dict = dict()
    for i, breed in enumerate(batch_breeds):
        if breed not in batch_breeds_dict.keys():
            batch_breeds_dict[breed] = [i]
        else:
            batch_breeds_dict[breed].append(i)

    st.title("Prédisez la race du chien sur une photo!")
    instructions = """
               Téléchargez votre propre image ou 
               sélectionnez-la dans la liste dans la barre latérale. 
               L'image que vous sélectionnez ou téléchargez 
               alimentera notre modèle de Deep Learning qui
               vous donnera sa prédiction sur la race du chien de l'image.
               """
    st.write(instructions)

    file = st.file_uploader("Veuillez importer une image")
    img_placeholder = st.empty()
    success = st.empty()
    submit_placeholder = st.empty()
    submit = False

    selected_breeds = st.sidebar.selectbox(
        "Race de chien", class_names)
    image_tensors_subset = batch_breeds_dict[selected_breeds]

    image_id = st.sidebar.selectbox("Identifiant de l'image", image_tensors_subset)
    
    with st.spinner("Chargement de l'image.."):
        if file:
            img_selected = Image.open(file)
            img_ready = prepare_image(img_selected)

            prediction = get_model_predictions(model, class_names, img_ready)

            available_images_id = batch_breeds_dict.get(prediction)
            nb_choice_available = len(available_images_id)-1

            examples_of_species = [i for i in np.random.choice(available_images_id, size=nb_choice_available)]
            examples_of_species = [batch_images[i].numpy()/255 for i in examples_of_species]

        else:
                nb_choice_available = len(image_tensors_subset) - 1

                examples_of_species = [i for i in np.random.choice(image_tensors_subset, size=nb_choice_available)]
                examples_of_species = [batch_images[i].numpy()/255 for i in examples_of_species]

                img_selected = batch_images[image_id].numpy()

                prediction = get_model_predictions(model, class_names, img_selected)

                img_selected = img_selected/255

    submit = submit_placeholder.button("Lancer la détection de race")

    if submit:
        st.title("Voici l'image que vous avez sélectionné :")
        st.image(img_selected)

        st.title(f"Le modèle pense que la race du chien est :")
        st.write(prediction)

        st.title(f"Voici {nb_choice_available} autre(s) image(s) de chien(s) de la race")
        st.write(prediction)
        st.image(examples_of_species)