# Contenido nuevo de Mates: ampliación de resúmenes, tarjetas y tema de problemas.
# La opción correcta va en la posición 0; la app baraja las opciones al mostrarlas.

EXTRA_HTML = {
'mat-pot': """<h5>Ejemplo resuelto</h5><p>Simplifica (2³ · 2⁵) : 2⁶</p><ul><li>Misma base multiplicando: 2³⁺⁵ = 2⁸</li><li>Dividiendo: 2⁸⁻⁶ = 2² = <b>4</b></li></ul>
<p>Notación científica: (3·10⁴)·(5·10⁻⁷) = 15·10⁻³ = <b>1,5·10⁻²</b> (deja una sola cifra antes de la coma).</p>
<h5>Porcentajes en una sola multiplicación</h5><ul><li>Subir un 15 %: × 1,15 · bajar un 20 %: × 0,80</li><li>Quitar el IVA del 21 %: ÷ 1,21 (no multipliques por 0,79)</li></ul>
<h5>Errores típicos</h5><ul><li>2³ · 3³ no es 6⁶: es (2·3)³ = 6³.</li><li>√(9 + 16) = 5, no 3 + 4 = 7: la raíz no se reparte en una suma.</li><li>(−2)² = 4, pero −2² = −4.</li></ul>""",
'mat-eq': """<h5>Ejemplo resuelto: 2.º grado</h5><p>x² − 5x + 6 = 0 → a = 1, b = −5, c = 6</p><ul><li>Δ = (−5)² − 4·1·6 = 25 − 24 = 1</li><li>x = (5 ± 1) / 2 → <b>x = 3</b> y <b>x = 2</b></li><li>Comprueba: 3² − 5·3 + 6 = 0 ✓</li></ul>
<h5>Ejemplo resuelto: sistema por reducción</h5><p>2x + y = 7 · x − y = 2. Sumando las dos: 3x = 9 → <b>x = 3</b>; y = 7 − 6 = <b>1</b>.</p>
<h5>Errores típicos</h5><ul><li>Olvidar el signo de b: si b = −5, entonces −b = +5.</li><li>x² = 9 tiene dos soluciones: 3 y −3.</li><li>Lo que multiplica pasa dividiendo (no restando).</li><li>Comprueba siempre la solución en la ecuación original: es un punto fácil.</li></ul>""",
'mat-suc': """<h5>Ejemplo resuelto</h5><p>Progresión aritmética con a₃ = 10 y a₇ = 22. Halla a₁ y S₁₀.</p><ul><li>d = (22 − 10) / (7 − 3) = 3</li><li>a₁ = a₃ − 2d = 10 − 6 = 4</li><li>a₁₀ = 4 + 9·3 = 31 → S₁₀ = 10·(4 + 31)/2 = <b>175</b></li></ul>
<p><b>Interés compuesto</b>: 1000 € al 5 % durante 2 años → 1000 · 1,05² = <b>1102,50 €</b> (con interés simple serían 1100 €).</p>
<h5>Errores típicos</h5><ul><li>Poner 5 en lugar de 1,05 en la fórmula del compuesto.</li><li>En la geométrica el exponente es n − 1, no n.</li><li>¿Se suma o se multiplica? Si la diferencia entre términos es fija → aritmética; si lo es el cociente → geométrica.</li></ul>""",
'mat-tri': """<h5>Ejemplo resuelto</h5><p>Desde 20 m de un edificio se ve la azotea con un ángulo de 35°. ¿Qué altura tiene?</p><ul><li>Dibuja el triángulo: conoces el <b>contiguo</b> (20 m) y buscas el <b>opuesto</b> (h) → tangente.</li><li>tan 35° = h / 20 → h = 20 · tan 35° ≈ 20 · 0,700 = <b>14,0 m</b></li></ul>
<h5>Valores que conviene saber</h5><ul><li>sen 30° = cos 60° = 0,5 · tan 45° = 1</li><li>sen 60° = cos 30° ≈ 0,866</li></ul>
<h5>Errores típicos</h5><ul><li>Calculadora en RAD: los resultados salen absurdos. Comprueba que pone DEG.</li><li>Confundir opuesto y contiguo: el opuesto es el lado que <i>no toca</i> el ángulo.</li><li>Pitágoras solo vale en triángulos rectángulos.</li></ul>""",
'mat-est': """<h5>Ejemplo resuelto: media con tabla</h5><p>Valores 1, 2, 3 con frecuencias 2, 3, 5 → media = (1·2 + 2·3 + 3·5) / (2 + 3 + 5) = 23 / 10 = <b>2,3</b></p>
<h5>Ejemplo resuelto: árbol</h5><p>El 60 % son mujeres y, de ellas, el 25 % va en bici → P(mujer y bici) = 0,6 · 0,25 = <b>0,15</b></p>
<h5>Errores típicos</h5><ul><li>Calcular la mediana sin ordenar los datos.</li><li>Con un número par de datos, la mediana es la media de los dos centrales.</li><li>Una probabilidad nunca pasa de 1: si te sale más, revisa.</li><li>P(no A) = 1 − P(A).</li></ul>""",
'mat-pol': """<h5>Ejemplo resuelto</h5><p>Factoriza P(x) = x³ − 6x² + 11x − 6</p><ul><li>Divisores de −6: ±1, ±2, ±3, ±6. Prueba x = 1: 1 − 6 + 11 − 6 = 0 ✓</li><li>Ruffini con 1: coeficientes 1 | −6 | 11 | −6 → cociente x² − 5x + 6, resto 0</li><li>x² − 5x + 6 = 0 → x = 2 y x = 3</li><li><b>P(x) = (x − 1)(x − 2)(x − 3)</b></li></ul>
<h5>Errores típicos</h5><ul><li>Olvidar el 0 del grado que falta: x³ − 4x + 2 → 1 | 0 | −4 | 2.</li><li>Con (x + 2) se pone −2 en Ruffini.</li></ul>""",
}

NEW_TOPIC = {
 "id": "mat-prob", "s": "mat", "title": "Problemas de enunciado",
 "blurb": "Del texto a la operación: el método y el diccionario",
 "html": """<p>Muchos ejercicios del examen vienen con texto. El método:</p><ol><li><b>Lee dos veces</b> y subraya los datos y la pregunta.</li><li><b>Nombra</b> lo que no sabes: x (y, si hace falta, y).</li><li><b>Traduce</b> cada frase a una ecuación u operación.</li><li><b>Resuelve</b> y <b>comprueba</b> con el enunciado. Escribe la respuesta con unidades.</li></ol>
<h5>Diccionario texto → matemáticas</h5><ul><li>«el doble de x» → 2x · «la mitad» → x/2 · «tres más que x» → x + 3</li><li>«hace 5 años» → x − 5 · «dentro de 5 años» → x + 5</li><li>«sube un 15 %» → × 1,15 · «rebaja del 30 %» → × 0,70 · «sin IVA (21 %)» → ÷ 1,21</li><li>«cada mes 10 € más» → aritmética (d = 10) · «se duplica cada hora» → geométrica (r = 2)</li><li>«se ve con un ángulo de…» → dibuja el triángulo y usa sen, cos o tan</li></ul>
<h5>Ejemplo</h5><p>Hace 5 años, Ana tenía el triple de edad que su hijo. Hoy Ana tiene 35. ¿Qué edad tiene el hijo?</p><ul><li>Hijo hoy: x. Hace 5 años: Ana tenía 30 y el hijo x − 5.</li><li>30 = 3(x − 5) → 30 = 3x − 15 → x = <b>15 años</b>.</li><li>Comprueba: hace 5 años tenían 30 y 10, y 30 = 3·10 ✓</li></ul>""",
}

# (tema, pregunta, [correcta, distractores...], explicación)
MC = [
# --- Potencias, raíces, notación, porcentajes ---
('mat-pot','2³ · 2⁴ =',['2⁷','2¹²','4⁷','2¹'],'Misma base multiplicando: se suman los exponentes, 3 + 4 = 7.'),
('mat-pot','5⁶ : 5² =',['5⁴','5³','1⁴','5⁸'],'Misma base dividiendo: se restan los exponentes, 6 − 2 = 4.'),
('mat-pot','(3²)³ =',['3⁶','3⁵','9⁵','3⁸'],'Potencia de potencia: se multiplican los exponentes, 2 · 3 = 6.'),
('mat-pot','2⁻³ =',['1/8','−8','−6','1/6'],'Exponente negativo: 2⁻³ = 1/2³ = 1/8.'),
('mat-pot','7⁰ =',['1','0','7','No existe'],'Cualquier número (distinto de 0) elevado a 0 vale 1.'),
('mat-pot','3,4 · 10⁻³ escrito en forma decimal es…',['0,0034','0,034','3400','0,00034'],'Exponente −3: la coma se mueve 3 lugares a la izquierda.'),
('mat-pot','45 000 000 en notación científica:',['4,5 · 10⁷','45 · 10⁶','4,5 · 10⁶','4,5 · 10⁸'],'Una sola cifra antes de la coma: 4,5 y la coma se ha movido 7 lugares.'),
('mat-pot','0,00062 en notación científica:',['6,2 · 10⁻⁴','6,2 · 10⁻³','62 · 10⁻⁵','6,2 · 10⁴'],'La coma se mueve 4 lugares a la derecha hasta 6,2 → exponente −4.'),
('mat-pot','(2 · 10³) · (4 · 10⁵) =',['8 · 10⁸','8 · 10¹⁵','6 · 10⁸','8 · 10⁷'],'Multiplica los números (2·4 = 8) y suma los exponentes (3 + 5 = 8).'),
('mat-pot','√50 simplificada:',['5√2','25√2','2√5','10√5'],'50 = 25 · 2 → √50 = √25 · √2 = 5√2.'),
('mat-pot','3√2 + 5√2 − √2 =',['7√2','8√2','7√6','7'],'Misma raíz: se suman los coeficientes, 3 + 5 − 1 = 7.'),
('mat-pot','√12 + √27 =',['5√3','√39','6√3','13√3'],'√12 = 2√3 y √27 = 3√3 → 2√3 + 3√3 = 5√3.'),
('mat-pot','log₂ 32 =',['5','16','6','30'],'2⁵ = 32, así que log₂ 32 = 5.'),
('mat-pot','log 1000 (en base 10) =',['3','100','4','30'],'10³ = 1000.'),
('mat-pot','2 + 3 · 4² =',['50','400','196','30'],'Primero la potencia (16), luego el producto (48) y al final la suma (50).'),
('mat-pot','Un abrigo de 85 € tiene un 20 % de descuento. Pagas…',['68 €','65 €','17 €','80 €'],'Bajar un 20 % es multiplicar por 0,80: 85 · 0,80 = 68 €.'),
('mat-pot','Un precio de 120 € sube un 15 %. Ahora cuesta…',['138 €','135 €','18 €','132 €'],'Subir un 15 % es multiplicar por 1,15: 120 · 1,15 = 138 €.'),
# --- Ecuaciones y sistemas ---
('mat-eq','3x − 5 = 10 → x =',['5','15','5/3','−5'],'3x = 15 → x = 5.'),
('mat-eq','2(x + 3) = 14 → x =',['4','7','5,5','8'],'2x + 6 = 14 → 2x = 8 → x = 4.'),
('mat-eq','x/3 + 2 = 5 → x =',['9','1','21','3'],'x/3 = 3 → x = 9.'),
('mat-eq','x² − 9 = 0',['x = 3 y x = −3','x = 3','x = 9','No tiene solución'],'x² = 9 → x = ±3. No olvides la solución negativa.'),
('mat-eq','x² − 5x = 0',['x = 0 y x = 5','x = 5','x = 0 y x = −5','x = √5'],'Factor común: x(x − 5) = 0 → x = 0 o x = 5.'),
('mat-eq','x² − 5x + 6 = 0',['x = 2 y x = 3','x = −2 y x = −3','x = 1 y x = 6','x = −1 y x = 6'],'Δ = 25 − 24 = 1 → x = (5 ± 1)/2 → 3 y 2.'),
('mat-eq','¿Cuántas soluciones reales tiene x² + 2x + 5 = 0?',['Ninguna','Dos','Una (doble)','Infinitas'],'Δ = 4 − 20 = −16 < 0: no hay soluciones reales.'),
('mat-eq','x² − 6x + 9 = 0',['x = 3 (solución doble)','x = −3','x = 3 y x = −3','No tiene solución'],'Δ = 36 − 36 = 0 → una solución doble: x = 6/2 = 3.'),
('mat-eq','Discriminante de 2x² + 3x − 2 = 0:',['25','−7','7','1'],'Δ = b² − 4ac = 9 − 4·2·(−2) = 9 + 16 = 25.'),
('mat-eq','2x² + 3x − 2 = 0',['x = 1/2 y x = −2','x = −1/2 y x = 2','x = 2 y x = −2','x = 1 y x = −2'],'x = (−3 ± 5)/4 → 2/4 = 1/2 y −8/4 = −2.'),
('mat-eq','Sistema: x + y = 10 · x − y = 4',['x = 7, y = 3','x = 3, y = 7','x = 6, y = 4','x = 8, y = 2'],'Sumando: 2x = 14 → x = 7; y = 10 − 7 = 3.'),
('mat-eq','Sistema: 2x + y = 7 · x − y = 2',['x = 3, y = 1','x = 1, y = 5','x = 2, y = 3','x = 4, y = −1'],'Sumando: 3x = 9 → x = 3; y = 7 − 6 = 1.'),
('mat-eq','Bicuadrada: x⁴ − 5x² + 4 = 0',['x = ±1 y x = ±2','x = 1 y x = 4','x = ±1 y x = ±4','No tiene solución'],'Con z = x²: z² − 5z + 4 = 0 → z = 1 o z = 4 → x = ±1, ±2.'),
('mat-eq','«Dos números suman 30 y uno es el doble del otro». La ecuación es…',['x + 2x = 30','x + 2 = 30','2x = 30 + x','x · 2x = 30'],'Uno es x y el otro 2x: x + 2x = 30 → x = 10 y 20.'),
('mat-eq','Entradas: adulto 8 €, niño 5 €. Se venden 50 y se recaudan 310 €. ¿Cuántas de adulto?',['20','30','25','15'],'a + n = 50 y 8a + 5n = 310 → 8a + 250 − 5a = 310 → a = 20.'),
# --- Polinomios ---
('mat-pol','Valor de P(x) = x² − 3x + 2 en x = 4:',['6','2','30','−2'],'16 − 12 + 2 = 6.'),
('mat-pol','Resto de (x³ − 2x + 1) : (x − 2):',['5','1','−3','0'],'Teorema del resto: P(2) = 8 − 4 + 1 = 5.'),
('mat-pol','Para dividir entre (x + 3) con Ruffini, a la izquierda pones…',['−3','3','1','0'],'(x + 3) = (x − (−3)) → a = −3.'),
('mat-pol','Coeficientes de x³ − 4x + 2 para Ruffini:',['1 | 0 | −4 | 2','1 | −4 | 2','1 | 4 | 2','0 | 1 | −4 | 2'],'Falta el término en x²: hay que poner un 0 en su lugar.'),
('mat-pol','¿Es x = 1 raíz de x³ − 6x² + 11x − 6?',['Sí, porque P(1) = 0','No, P(1) = −6','No, P(1) = 12','Solo si x = 6'],'P(1) = 1 − 6 + 11 − 6 = 0.'),
('mat-pol','x³ − 6x² + 11x − 6 factorizado:',['(x − 1)(x − 2)(x − 3)','(x + 1)(x + 2)(x + 3)','(x − 1)(x − 6)','x(x − 6)(x + 11)'],'Raíces 1, 2 y 3 (Ruffini con 1 y luego la fórmula).'),
('mat-pol','(x + 5)² =',['x² + 10x + 25','x² + 25','x² + 5x + 25','x² + 10x + 10'],'(a + b)² = a² + 2ab + b² → x² + 10x + 25.'),
('mat-pol','(2x − 3)² =',['4x² − 12x + 9','4x² − 9','4x² − 6x + 9','2x² − 12x + 9'],'(2x)² − 2·2x·3 + 3² = 4x² − 12x + 9.'),
('mat-pol','(x + 4)(x − 4) =',['x² − 16','x² + 16','x² − 8x − 16','x² − 8'],'Suma por diferencia: a² − b².'),
('mat-pol','x² − 49 factorizado:',['(x + 7)(x − 7)','(x − 7)²','(x + 49)(x − 1)','x(x − 49)'],'Diferencia de cuadrados: a² − b² = (a + b)(a − b).'),
('mat-pol','Raíces enteras posibles de x³ + 2x² − 5x − 6:',['±1, ±2, ±3, ±6','±1, ±5','±2, ±5','1, 2, 5, 6'],'Son los divisores del término independiente, −6.'),
('mat-pol','Ruffini de (x² − 5x + 6) : (x − 2):',['Cociente x − 3, resto 0','Cociente x + 3, resto 0','Cociente x − 3, resto 2','Cociente x − 7, resto 20'],'1 | −5 | 6 con 2: baja 1; −5 + 2 = −3; 6 − 6 = 0.'),
('mat-pol','Grado de (x² + 1)(x³ − x):',['5','6','3','2'],'Al multiplicar se suman los grados: 2 + 3 = 5.'),
# --- Progresiones e interés ---
('mat-suc','3, 7, 11, 15… La diferencia d es…',['4','3','7','11'],'Cada término suma 4 al anterior.'),
('mat-suc','Término general de 3, 7, 11, 15…',['aₙ = 4n − 1','aₙ = 4n + 3','aₙ = 3n + 4','aₙ = 3 · 4ⁿ⁻¹'],'aₙ = 3 + (n − 1)·4 = 4n − 1.'),
('mat-suc','En 3, 7, 11… el término a₂₀ es…',['79','83','80','76'],'a₂₀ = 4·20 − 1 = 79.'),
('mat-suc','Suma de los 20 primeros términos de 3, 7, 11…',['820','1640','790','860'],'S₂₀ = 20 · (3 + 79) / 2 = 820.'),
('mat-suc','Aritmética con a₃ = 10 y a₇ = 22. d =',['3','4','12','6'],'d = (22 − 10) / (7 − 3) = 3.'),
('mat-suc','2, 6, 18, 54… La razón r es…',['3','4','2','6'],'Cada término se multiplica por 3.'),
('mat-suc','En 2, 6, 18… el término a₆ es…',['486','1458','162','96'],'a₆ = 2 · 3⁵ = 2 · 243 = 486.'),
('mat-suc','80, 40, 20, 10… La razón es…',['1/2','−40','2','−1/2'],'Cada término es la mitad del anterior: r = 1/2.'),
('mat-suc','5, 10, 20, 40… es una progresión…',['Geométrica, r = 2','Aritmética, d = 5','Aritmética, d = 10','No es progresión'],'El cociente es constante (× 2), la diferencia no.'),
('mat-suc','Interés simple: 2000 € al 3 % durante 4 años. Intereses:',['240 €','2240 €','24 €','251,02 €'],'I = 2000 · 3 · 4 / 100 = 240 €.'),
('mat-suc','Interés compuesto: 1000 € al 5 % durante 2 años. Capital final:',['1102,50 €','1100,00 €','1105,00 €','1050,00 €'],'1000 · 1,05² = 1102,50 €.'),
('mat-suc','Interés compuesto: 5000 € al 4 % durante 3 años. Capital final:',['5624,32 €','5600,00 €','5800,00 €','5208,00 €'],'5000 · 1,04³ = 5000 · 1,124864 = 5624,32 €.'),
('mat-suc','A más de un año, ¿qué da más dinero?',['El interés compuesto','El interés simple','Dan lo mismo','Depende del capital'],'En el compuesto, los intereses también generan intereses.'),
# --- Trigonometría ---
('mat-tri','Catetos 6 y 8. La hipotenusa mide…',['10','14','48','√28'],'√(36 + 64) = √100 = 10.'),
('mat-tri','Hipotenusa 13 y un cateto 5. El otro cateto mide…',['12','8','√194','18'],'√(169 − 25) = √144 = 12.'),
('mat-tri','Opuesto 3 e hipotenusa 5: sen α =',['3/5','4/5','3/4','5/3'],'sen = opuesto / hipotenusa.'),
('mat-tri','Opuesto 3 y contiguo 4: tan α =',['3/4','4/3','3/5','4/5'],'tan = opuesto / contiguo.'),
('mat-tri','Un triángulo tiene ángulos de 50° y 60°. El tercero mide…',['70°','90°','110°','80°'],'180 − 50 − 60 = 70°.'),
('mat-tri','Escalera de 5 m con el pie a 3 m de la pared. ¿A qué altura llega?',['4 m','2 m','√34 m','8 m'],'√(25 − 9) = √16 = 4 m.'),
('mat-tri','Si tan α = 1, α =',['45°','30°','60°','90°'],'Opuesto = contiguo → triángulo isósceles → 45°.'),
('mat-tri','sen 30° =',['0,5','0,866','1','0,707'],'Valor que conviene saber: sen 30° = 1/2.'),
('mat-tri','cos 60° =',['0,5','0,866','0','1'],'cos 60° = sen 30° = 1/2.'),
('mat-tri','Antes de usar arctan, la calculadora debe estar en…',['Grados (DEG)','Radianes (RAD)','GRAD','Da igual'],'En el examen los ángulos van en grados.'),
('mat-tri','Un árbol da 10 m de sombra cuando el sol forma 40° con el suelo. Altura:',['≈ 8,39 m','≈ 6,43 m','≈ 7,66 m','≈ 11,92 m'],'Contiguo 10, buscas el opuesto: h = 10 · tan 40° ≈ 8,39 m.'),
('mat-tri','Lados 5 y 7 con 60° entre ellos. El tercer lado mide…',['√39 ≈ 6,24','√74 ≈ 8,60','12','√109 ≈ 10,44'],'Teorema del coseno: 25 + 49 − 2·5·7·0,5 = 39.'),
('mat-tri','¿Cuándo usas el teorema del coseno?',['Triángulo no rectángulo con dos lados y el ángulo entre ellos','Triángulo rectángulo con los dos catetos','Para sumar ángulos','Nunca sale en el examen'],'Si el triángulo es rectángulo, basta con Pitágoras y SOH-CAH-TOA.'),
# --- Estadística y probabilidad ---
('mat-est','Media de 4, 6, 8, 10, 12:',['8','10','40','6'],'40 / 5 = 8.'),
('mat-est','Mediana de 3, 9, 4, 7, 1:',['4','7','5','4,8'],'Ordenados: 1, 3, 4, 7, 9 → el central es 4.'),
('mat-est','Mediana de 2, 5, 8, 10:',['6,5','5','8','6,25'],'Número par de datos: (5 + 8) / 2 = 6,5.'),
('mat-est','Moda de 2, 3, 3, 5, 7, 3, 5:',['3','5','4','7'],'El 3 aparece tres veces.'),
('mat-est','Rango de 12, 4, 9, 20, 7:',['16','20','8','4'],'Máximo − mínimo = 20 − 4 = 16.'),
('mat-est','Valores 1, 2, 3 con frecuencias 2, 3, 5. Media:',['2,3','2','6','3'],'(2 + 6 + 15) / 10 = 2,3.'),
('mat-est','Dado: P(sacar más de 4)',['1/3','1/2','2/3','1/6'],'Favorables: 5 y 6 → 2/6 = 1/3.'),
('mat-est','Urna con 3 rojas, 5 azules y 2 verdes. P(azul)',['1/2','5/8','1/5','1/3'],'5 / 10 = 1/2.'),
('mat-est','Lanzas dos monedas. P(dos caras)',['1/4','1/2','1/3','3/4'],'Casos: CC, CX, XC, XX → 1 de 4.'),
('mat-est','Dos dados. P(que sumen 7)',['1/6','7/36','1/12','1/7'],'6 casos favorables de 36: (1,6), (2,5)… → 6/36.'),
('mat-est','Si P(A) = 0,3, entonces P(no A) =',['0,7','0,3','1,3','0'],'P(no A) = 1 − P(A).'),
('mat-est','El 60 % son mujeres y, de ellas, el 25 % va en bici. P(mujer y bici)',['0,15','0,85','0,35','0,25'],'En el árbol se multiplica: 0,6 · 0,25 = 0,15.'),
('mat-est','Nube de puntos que sube hacia la derecha, muy pegada a una recta:',['Correlación lineal positiva fuerte','Correlación negativa débil','Correlación nula','Curvilínea negativa'],'Sube → positiva; pegada a una recta → lineal y fuerte (r cerca de 1).'),
('mat-est','Clase de 40: 16 chicas, y 4 de ellas llevan gafas. Si eliges una chica, P(gafas)',['1/4','1/10','2/5','3/4'],'Condicionada: se divide entre las chicas, 4/16 = 1/4.'),
# --- Problemas de enunciado ---
('mat-prob','Un móvil cuesta 240 € con el 21 % de IVA incluido. Sin IVA cuesta…',['198,35 €','189,60 €','219,00 €','290,40 €'],'Quitar el IVA es dividir: 240 / 1,21 ≈ 198,35 €. (240 · 0,79 es un error típico.)'),
('mat-prob','Tras una rebaja del 30 % pagas 56 €. Precio original:',['80 €','72,80 €','39,20 €','86 €'],'Precio · 0,70 = 56 → precio = 56 / 0,70 = 80 €.'),
('mat-prob','Un depósito tiene 1500 L y pierde 40 L al día. ¿Cuántos días hasta que queden 300 L?',['30','37,5','45','7,5'],'Tiene que perder 1200 L: 1200 / 40 = 30 días.'),
('mat-prob','Ahorras 50 € el primer mes y cada mes 10 € más. ¿Cuánto en un año?',['1260 €','1660 €','600 €','1200 €'],'Aritmética: a₁₂ = 50 + 11·10 = 160; S₁₂ = 12·(50 + 160)/2 = 1260 €.'),
('mat-prob','2000 bacterias se duplican cada hora. ¿Cuántas hay a las 5 horas?',['64 000','32 000','10 000','20 000'],'Geométrica: 2000 · 2⁵ = 64 000.'),
('mat-prob','Un rectángulo tiene 36 cm de perímetro y el largo es el doble del ancho. Medidas:',['6 cm y 12 cm','9 cm y 18 cm','12 cm y 24 cm','6 cm y 18 cm'],'2(x + 2x) = 36 → 6x = 36 → x = 6 y el largo 12.'),
('mat-prob','Hace 4 años Luis tenía el doble de edad que su hija. Hoy Luis tiene 40. ¿Y la hija?',['22','20','18','24'],'36 = 2(x − 4) → x − 4 = 18 → x = 22.'),
('mat-prob','3 kg de manzanas y 2 kg de peras: 9,50 €. 1 kg de manzanas y 2 kg de peras: 5,50 €. ¿Kilo de manzanas?',['2 €','1,75 €','2,50 €','1,50 €'],'Restando las dos ecuaciones: 2m = 4 → m = 2 €.'),
('mat-prob','Una rampa de 6 m sube 1,5 m de altura. ¿Qué ángulo forma con el suelo?',['≈ 14,5°','≈ 14,0°','≈ 75,5°','≈ 0,25°'],'La rampa es la hipotenusa: sen α = 1,5/6 = 0,25 → α ≈ 14,5°.'),
('mat-prob','Desde 20 m de un edificio se ve la azotea con 35°. Altura:',['≈ 14,0 m','≈ 11,5 m','≈ 16,4 m','≈ 28,6 m'],'Contiguo conocido, buscas el opuesto: h = 20 · tan 35° ≈ 14,0 m.'),
('mat-prob','En un grupo de 30 personas, 12 hablan inglés. P(que una al azar no lo hable)',['3/5','2/5','1/2','1/18'],'No lo hablan 18: 18/30 = 3/5.'),
('mat-prob','Notas 5, 7, 6 y x. La media es 6,5. ¿Cuánto vale x?',['8','6,5','7','9'],'La suma debe ser 4 · 6,5 = 26 → x = 26 − 18 = 8.'),
('mat-prob','3000 € al 2 % anual compuesto durante 10 años. ¿Qué expresión da el capital final?',['3000 · 1,02¹⁰','3000 · 1,2¹⁰','3000 · (1 + 0,02 · 10)','3000 · 0,02¹⁰'],'Cf = C · (1 + r/100)ᵗ = 3000 · 1,02¹⁰. La tercera es interés simple.'),
]

TITLES = {'mat-pot':'Potencias, raíces y notación','mat-eq':'Ecuaciones y sistemas','mat-pol':'Polinomios y Ruffini',
          'mat-suc':'Progresiones e interés','mat-tri':'Trigonometría','mat-est':'Estadística y probabilidad',
          'mat-prob':'Problemas de enunciado'}

def cards():
    out=[]; n={}
    for t,q,o,e in MC:
        assert len(set(o))==len(o),q
        n[t]=n.get(t,0)+1
        out.append({"id":f"matx-{t[4:]}{n[t]}","k":"mc","s":"mat","t":t,"topic":TITLES[t],"q":q,"o":o,"a":0,"e":e})
    return out
