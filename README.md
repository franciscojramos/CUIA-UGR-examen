#  CUIA-UGR-examen
Examen interactivo (tipo test) de **Computación Ubicua e Inteligencia Ambiental**  
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
## ¿Qué hace este proyecto?  
`quiz.py` lanza un cuestionario en terminal para repasar la asignatura:  
1. `preguntas.json` (125 preguntas máx).  
2. Te pide cuántas preguntas quieres contestar.  
3. Muestra las preguntas aleatoriamente ,cada enunciado con opciones **a-d**; registras tu respuesta.  
4. Corrige al momento, da explicación detallada y va contando aciertos.  
5. Al final puedes repetir las falladas.  

> **Ejemplo rápido**
> ```bash
> $ python3 quiz.py
> ¿Cuántas preguntas quieres responder? (máx 125): 25
> 🚀  Comienza el examen interactivo
> ...
> 🏁  Resultados finales
>    🏆  Aciertos: 22
>    ❌  Fallos: 3
> 🔁  ¿Repetir solo las falladas? (s/n):
> ```

## Instalación  
```bash
git clone hhttps://github.com/franciscojramos/CUIA-UGR-examen)
python3 quiz.py
```
## Autor
**Francisco José Ramos Moya** – código y organización de preguntas.

## Créditos
Algunas preguntas se basan en apuntes de **martasw99** subidos a *Wuolah*.

## Descargo de responsabilidad
Este repositorio es **solo orientativo** para estudiar; puede contener preguntas o explicaciones incorrectas.  
El autor **no se hace responsable** de errores ni de los resultados obtenidos en exámenes.  
¡Úsalo bajo tu propio criterio y contrástalo siempre con la bibliografía oficial!

## Contribuir
- Haz un *fork*.  
- Añade o corrige preguntas en el mismo formato **JSON**.  
- Abre un *pull request*.
