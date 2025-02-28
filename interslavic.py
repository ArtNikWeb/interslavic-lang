Mežslavjansky Jezyk Programovanja (ISL)

Vvedenje

ISL (Mežslavjansky Jezyk) je prosty interpretovany jezyk programovanja, osnovany na mežslavjanskom jezyku. On jest sozdany da byti razumlivy i intuitivny za slavjanov. Jezyk poddržava bazičny konstrukcije kako promenljive, aritmetične operacije, uslovne operatori, cikly i vyvod teksta.

Funkcije
 • Promenljive: Cele čislo (cele čislo), Drobno čislo (drobno čislo), Tekst (tekst)
 • Aritmetične operacije
 • Uslovne konstrukcije: ako ... inakse ...
 • Cikly: povtorjaj (i od X do Y)
 • Vyvod v konzolu: pečati(...)

Primer koda

cele čislo x = 5;
ako (x > 3) {
    pečati("Čislo je vyše od 3");
} inakse {
    pečati("Čislo je menše od 3");
}

povtorjaj (i od 1 do 5) {
    pečati("Cikl: " + i);
}

Kako on raboti
 1. Upotrebljaj promenljive s naturalnymi slavjanskymi slovami.
 2. Primenjaj uslovi za kontrolovanje koda.
 3. Upotrebljaj cikly za povtorjenje operaciji.
 4. Vyvodi tekst s pečati(...).

Instalacija i Upotreba
 1. Skloniraj repozytorij:

git clone https://github.com/yourusername/interslavic-lang.git
cd interslavic-lang


 2. Zapusti interpretator:

python interslavic.py example.isl

---

## **2. `interslavic.py` (Интерпретатор)**
Создай файлky Jezyk Programovanи вставь туда этот код:

```python
import re

class InterslavicInterpreter:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expr):
        """Оценка математического выражения."""
        try:
            return eval(expr, {}, self.variables)
        except Exception:
            return expr.strip('"')

    def execute(self, code):
        """Обрабатывает и выполняет код."""
        lines = code.split("\n")
        output = []
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if not line:
                i += 1
                continue

            var_match = re.match(r"(cele čislo|drobno čislo|tekst) (\w+) = (.+);", line)
            if var_match:
                _, var_name, value = var_match.groups()
                self.variables[var_name] = self.evaluate_expression(value)
                i += 1
                continue

            print_match = re.match(r'pečati\((.+)\);', line)
            if print_match:
                value = self.evaluate_expression(print_match.group(1))
                output.append(str(value))
                print(value)
                i += 1
                continue

            if line.startswith("ako "):
                condition = line[4:-2]
                if self.evaluate_expression(condition):
                    i += 1
                    continue
                else:
                    while i < len(lines) and not lines[i].strip().startswith("inakse"):
                        i += 1
                i += 1
                continue

            loop_match = re.match(r"povtorjaj \((\w+) od (\d+) do (\d+)\) {", line)
            if loop_match:
                var_name, start, end = loop_match.groups()
                start, end = int(start), int(end)
                for value in range(start, end + 1):
                    self.variables[var_name] = value
                    loop_body = []
                    i += 1
                    while i < len(lines) and not lines[i].strip().startswith("}"):
                        loop_body.append(lines[i])
                        i += 1
                    for loop_line in loop_body:
                        self.execute(loop_line)
                i += 1
                continue
            
            i += 1

        return "\n".join(output)

if(value))
 == "__main__":
    with open("example.isl", "r", encoding="utf-8") as f:
        code = f.read()
    
    interpreter = InterslavicInterpreter()
    interpreter.execute(code)
