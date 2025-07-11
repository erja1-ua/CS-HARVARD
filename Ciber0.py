{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/erja1-ua/CS-HARVARD/blob/Leccion0/Ciber0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Importa todas las letras del alfabeto (mayúsculas + minúsculas)\n",
        "from string import ascii_letters\n",
        "\n",
        "# Bucle anidado que recorre todas las combinaciones posibles de 4 letras\n",
        "for i in ascii_letters:\n",
        "    for j in ascii_letters:\n",
        "        for k in ascii_letters:\n",
        "            for l in ascii_letters:\n",
        "                print(i, j, k, l)  # Imprime una combinación de 4 letras (por ejemplo: A b C d)"
      ],
      "metadata": {
        "id": "B6RXl14tbdnj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from string import ascii_letters, digits, punctuation\n",
        "\n",
        "for i in ascii_letters + digits + punctuation:\n",
        "    for j in ascii_letters + digits + punctuation:\n",
        "        for k in ascii_letters + digits + punctuation:\n",
        "            for l in ascii_letters + digits + punctuation:\n",
        "                print(i, j, k, l)"
      ],
      "metadata": {
        "id": "HFiVmn3Se0dO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NPTXFhjFYnRE"
      },
      "outputs": [],
      "source": [
        "from string import ascii_letters, digits, punctuation\n",
        "# Importa tres conjuntos de caracteres:\n",
        "# ascii_letters: letras mayúsculas y minúsculas (A–Z, a–z)\n",
        "# digits: números del 0 al 9\n",
        "# punctuation: símbolos como !@#$%^&*()_+ etc.\n",
        "\n",
        "# Bucle anidado que genera todas las combinaciones posibles de 4 caracteres\n",
        "# usando letras, dígitos y símbolos\n",
        "for i in ascii_letters + digits + punctuation:\n",
        "    for j in ascii_letters + digits + punctuation:\n",
        "        for k in ascii_letters + digits + punctuation:\n",
        "            for l in ascii_letters + digits + punctuation:\n",
        "                # Imprime cada combinación de 4 caracteres separados por espacios\n",
        "                print(i, j, k, l)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "## Enumerar contraseñas de 1 a 4 dígitos (números)\n",
        "## itertools.product(...) genera el producto cartesiano de iterables.\n",
        "from itertools import product\n",
        "from string import digits\n",
        "\n",
        "## CONTRASEÑA OBJETIVO\n",
        "target_password = \"1234\"\n",
        "\n",
        "#Generador de combinaciones\n",
        "def crack_numeric(length):\n",
        "    # Recorre todas las combinaciones posibles de 'length' dígitos\n",
        "    for combo in product(digits, repeat=length):\n",
        "        # Une los caracteres del tuple 'combo' en una cadena (por ejemplo: ('1','2','3') → \"123\")\n",
        "        guess = ''.join(combo)\n",
        "\n",
        "        # Compara la combinación generada con la contraseña objetivo\n",
        "        if guess == target_password:\n",
        "            # Si coincide, imprime mensaje y termina la función\n",
        "            print(\"Contraseña encontrada :D =>\", guess)\n",
        "            return\n",
        "\n",
        "    # Si el bucle termina sin encontrarla, muestra este mensaje (¡pero ojo, está mal indentado!)\n",
        "    print(\"Contraseña no encontrada :(\")\n",
        "\n",
        "#Ejecutamos el algoritmo\n",
        "crack_numeric(4)\n",
        "\n",
        "\n",
        "## def crack_numeric(length):      ## recibe un entero\n",
        "##     for combo in product(digits, repeat=length): ## genera todas las combinaciones posibles con logitud length\n",
        "##         yield ''.join(combo)    ## devuelve un generador que produce todas las combinaciones de length\n",
        "## El uso de yield convierte la función en un generador,\n",
        "##que va devolviendo resultados uno a uno en vez de construir toda la lista en memoria\n",
        "\n",
        "## for pwd in crack_numeric(4): ## recorre todas las contraseñas posibles de x digitos este ejemplo 4\n",
        "##     pass # simula comparación segura\n",
        "## En este ejemplo, no se hace nada (pass),\n",
        "## pero se podría comparar con una contraseña objetivo.\n",
        "## print(\"Listas generadas:\", 10**4)"
      ],
      "metadata": {
        "id": "rSnsmq1Hi0kI"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
