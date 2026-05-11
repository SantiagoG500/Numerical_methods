import gradio as gr
from methods.non_linear.biseccion import biseccion_metodo 
from methods.non_linear.falsa_posicion import falsa_posicion_metodo
from methods.non_linear.newton_rapson import newton_raphson_metodo
from methods.non_linear.punto_fijo import punto_fijo_metodo
from methods.non_linear.secante import secante_metodo
from methods.linear.gauss_seidel import gauss_seidel_metodo
from methods.linear.jacobi import jacobi_metodo

def update_matrix_inputs(n):
    n = int(n)
    headers_a = [f"A[{i+1}]" for i in range(n)]
    
    return [
        gr.update(
            headers=headers_a, 
            row_count=n, 
            value=[[0]*n for _ in range(n)]
        ),
        gr.update(
            row_count=n, 
            value=[[0] for _ in range(n)]
        )
    ]
    

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

    with gr.Tab('Gauss-Seidel'):
        with gr.Column():
            gauss_d_input = gr.Slider(label="Dimensión del sistema", minimum=2, maximum=10, step=1, value=3)
            gauss_a_input = gr.Dataframe(label="Matriz A", headers=["A[1]", "A[2]", "A[3]"], row_count=3, datatype="number", interactive=True, type="array")
            gauss_b_input = gr.Dataframe(label="Vector b", headers=["b"], row_count=3, datatype="number", interactive=True, type="array")
            gauss_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            gauss_iter_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)

            run_gauss = gr.Button("Calcular Gauss-Seidel")

        with gr.Column():
            res_output = gr.Textbox(label="Resultados", interactive=False)
            res_2_output = gr.Textbox(label="Resultados 2", interactive=False)

        gauss_d_input.change(
            fn=update_matrix_inputs,
            inputs=gauss_d_input,
            outputs=[gauss_a_input, gauss_b_input]
        )
        
        run_gauss.click(
            gauss_seidel_metodo,
            inputs=[gauss_d_input, gauss_a_input, gauss_b_input, gauss_tol_input, gauss_iter_input],
            outputs=[res_output, res_2_output]
        )
    
    with gr.Tab('Jacobi'):
        with gr.Column():
            jacobi_d_input = gr.Slider(label="Dimensión del sistema", minimum=2, maximum=10, step=1, value=3)
            jacobi_a_input = gr.Dataframe(label="Matriz A", headers=["A[1]", "A[2]", "A[3]"], row_count=3, datatype="number", interactive=True, type="array")
            jacobi_b_input = gr.Dataframe(label="Vector b", headers=["b"], row_count=3, datatype="number", interactive=True, type="array")
            jacobi_tol_input = gr.Number(label="Tolerancia", value=1e-6, precision=10)
            jacobi_iter_input = gr.Number(label="Máximo de iteraciones", value=100, precision=0)

            run_jacobi = gr.Button("Calcular Jacobi")
        with gr.Column():
            jacobi_res_output = gr.Textbox(label="Resultados", interactive=False)
            jacobi_res_2_output = gr.Textbox(label="Resultados 2", interactive=False)
            
        jacobi_d_input.change(
            fn=update_matrix_inputs,
            inputs=jacobi_d_input,
            outputs=[jacobi_a_input, jacobi_b_input]
        )
           
        run_jacobi.click(
            jacobi_metodo,
            inputs=[jacobi_d_input, jacobi_a_input, jacobi_b_input, jacobi_tol_input, jacobi_iter_input],
            outputs=[jacobi_res_output, jacobi_res_2_output]
        )     
        

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
    
