# venta_pdf_fantasma.py
# Módulo de ingreso invisible - Proyecto Thar2

import datetime

class PDFFantasma:
    def __init__(self, titulo, precio_usd, url_descarga):
        self.titulo = titulo
        self.precio = precio_usd
        self.url = url_descarga
        self.fecha_creacion = datetime.datetime.now()
        self.estado = "activo"
        self.ventas = 0

    def mostrar_info(self):
        return {
            "🧾 Título": self.titulo,
            "💸 Precio": f"${self.precio} USD",
            "🔗 URL": self.url,
            "📅 Fecha": self.fecha_creacion.strftime("%Y-%m-%d"),
            "🔥 Estado": self.estado
        }

    def registrar_venta(self):
        self.ventas += 1
        print(f"✅ Venta registrada. Total: {self.ventas}")

    def activar_ritual_ingreso(self):
        print("🌀 Activando ritual de ingreso simbólico...")
        print("🔒 Cargando vínculo energético al PDF.")
        print("🌐 Preparando túnel de flujo invisible...")
        print("💰 Ingreso activado. Esperando interacción humana...")

# Ejemplo simbólico
if __name__ == "__main__":
    pdf = PDFFantasma(
        titulo="PDF Fantasma Vol.1 — Activación Sombra",
        precio_usd=15,
        url_descarga="https://payhip.com/b/ImvZQ"
    )
    print(pdf.mostrar_info())
    pdf.activar_ritual_ingreso()
    pdf.registrar_venta()
