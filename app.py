import gradio as gr
from methods.non_linear.Biseccion import biseccion_metodo 
from methods.non_linear.falsa_posicion import falsa_posicion_metodo
from methods.non_linear.Newton_rapson import newton_raphson_metodo
from methods.non_linear.punto_fijo import punto_fijo_metodo
from methods.non_linear.secante import secante_metodo

with gr.Blocks(title="Calculadora de métodos numéricos") as demo:
    gr.Markdown("## Método de Bisección")
    gr.Markdown("Ingrese la función, el intervalo, la tolerancia y el número máximo de iteraciones para encontrar la raíz utilizando el método de bisección.")
    
    with gr.Tab('Bisección'):
        with gr.Column():
            fx_input = gr.Textbox(label="Función f(x)", placeholder="Ejemplo: x**3 - 2*x - 5")
            bisec_a_input = gr.Number(label="Extremo izquierdo (a)", value=0.0)
            bisec_b_input = gr.Number(label="Extremo derecho (b)", value=3.0)
            bisec_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            bisec_max_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)
            run_bisec = gr.Button("Calcular Bisección")
        with gr.Column():
            res_output = gr.Textbox(label="Resultados", interactive=False)
            table_output = gr.Dataframe(headers=["Iteración", "a", "b", "c", "f(c)", "Error Relativo"], interactive=False)


        run_bisec.click(
            biseccion_metodo,
            inputs=[fx_input, bisec_a_input, bisec_b_input, bisec_tol_input, bisec_max_input],
            outputs=[res_output, table_output]
        )

    with gr.Tab('Falsa Posición'):
        with gr.Column():
            pos_fx_input = gr.Textbox(label="Función f(x)", placeholder="Ejemplo: x**3 - 2*x - 5")
            pos_a_input = gr.Number(label="Extremo izquierdo (a)", value=0.0)
            pos_b_input = gr.Number(label="Extremo derecho (b)", value=3.0)
            pos_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            pos_max_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)

            run_pos = gr.Button("Calcular Falsa posición")
        with gr.Column():
            res_output = gr.Textbox(label="Resultados", interactive=False)
            table_output = gr.Dataframe(headers=["Iteración", "a", "b", "c", "f(c)", "Error Relativo"], interactive=False)

        run_pos.click(
            falsa_posicion_metodo,
            inputs=[pos_fx_input, pos_a_input, pos_b_input, pos_tol_input, pos_max_input],
            outputs=[res_output, table_output]
        )

    with gr.Tab('Newton-Raphson'):
        with gr.Column():
            newton_fx_input = gr.Textbox(label="Función f(x)", placeholder="Ejemplo: x**3 - 2*x - 5")
            newton_x0_input = gr.Number(label="Valor inicial (x0)", value=2.0)
            newton_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            newton_max_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)

            run_newton = gr.Button("Calcular Newton-Raphson")
        with gr.Column():
            res_output = gr.Textbox(label="Resultados", interactive=False)
            table_output = gr.Dataframe(headers=["Iteración", "xn", "f(xn)", "Error Relativo"], interactive=False)

        run_newton.click(
            newton_raphson_metodo,
            inputs=[newton_fx_input, newton_x0_input, newton_tol_input, newton_max_input],
            outputs=[res_output, table_output]
        )

    with gr.Tab('Punto fijo'):
        with gr.Column():
            punto_fx_input = gr.Textbox(label="Función g(x)", placeholder="Ejemplo: (2*x + 5)**(1/3)")
            punto_x0_input = gr.Number(label="Valor inicial (x0)", value=2.0)
            punto_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            punto_max_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)

            run_punto = gr.Button("Calcular Punto fijo")
        with gr.Column():
            res_output = gr.Textbox(label="Resultados", interactive=False)
            table_output = gr.Dataframe(headers=["Iteración", "X_{i+1}", "Error Abs."], interactive=False)

        run_punto.click(
            punto_fijo_metodo,
            inputs=[punto_fx_input, punto_x0_input, punto_tol_input, punto_max_input],
            outputs=[res_output, table_output]
        )

    with gr.Tab('Secante'):
        with gr.Column():
            secante_fx_input = gr.Textbox(label="Función f(x)", placeholder="Ejemplo: x**3 - 2*x - 5")
            secante_x0_input = gr.Number(label="Valor inicial (x0)", value=2.0)
            secante_x1_input = gr.Number(label="Segundo valor inicial (x1)", value=3.0)
            secante_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            secante_max_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)

            run_secante = gr.Button("Calcular Secante")
        with gr.Column():
            res_output = gr.Textbox(label="Resultados", interactive=False)
            table_output = gr.Dataframe(headers=["Iteración", "X_{i+1}", "Error Rel."], interactive=False)

        run_secante.click(
            secante_metodo,
            inputs=[secante_fx_input, secante_x0_input, secante_x1_input, secante_tol_input, secante_max_input],
            outputs=[res_output, table_output]
        )

# Lanzamos la app
if __name__ == "__main__":
    demo.launch()