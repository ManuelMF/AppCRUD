package Controlador;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.math.BigDecimal;
import java.math.RoundingMode;

import javax.swing.JOptionPane;

import Modelo.Producto;

public class Lista {
	Vista.Lista Ventana;
	public Lista() {
		Ventana = new Vista.Lista();
		
		Ventana.btnA�adir.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				anyadirProductoALista();
			}
		});
		
		Ventana.btnDelete.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				delProductoALista();
			}
		});
		
		Ventana.btnVaciar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				vaciarProductoALista();
			}
		});
		
		Ventana.btnA�adir_lista.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				anyadirProducto();
			}
		});
		
		Ventana.btnDelete_lista.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				deleteProducto();
			}
		});
		
		Ventana.btnVaciar_lista.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				vaciarProducto();
			}
		});
		
		Ventana.btnChange.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				change();
			}
		});
	}
	
	public boolean contiene(Producto p, Vista.Lista Ventana) {
		
		for(int x=0; x< Ventana.modeloLista.getSize() ; x++) {
			if (p.equals(Ventana.modeloLista.getElementAt(x))) return true;
		}
		
		return false;
	}
	
	private void anyadirProductoALista() {
		Producto p = (Producto) Ventana.listProductos.getSelectedValue();
		
		if (contiene(p,Ventana)) {
			JOptionPane.showMessageDialog(null, "Producto ya a�adido","ERROR",JOptionPane.ERROR_MESSAGE);
		} else {
			Ventana.modeloLista.addElement(p);
			calcularTotal();
		}
	}
	
	private void delProductoALista() {
		Producto p = (Producto) Ventana.list_Lista.getSelectedValue();
		Ventana.modeloLista.removeElement(p); 
		calcularTotal();
		
		
	}
	
	private void vaciarProductoALista() {
		Ventana.modeloLista.removeAllElements(); 
		calcularTotal();
	}
	
	private void anyadirProducto() {
		
		String nombrep = JOptionPane.showInputDialog ( "Nombre del producto:" );
		boolean error = true;
		double precio = 0;
		do {
			try {
				String preciop = JOptionPane.showInputDialog ( "Precio del producto:" );
				precio=Double.parseDouble(preciop);
				error=false;
			} catch (Exception e) {
				JOptionPane.showMessageDialog(null, "Introduce un numero","ERROR",JOptionPane.ERROR_MESSAGE);
			}
		
		} while(error);
		
		Producto p =new Producto(nombrep,precio);
		 
		if (contiene(p,Ventana)) {
			JOptionPane.showMessageDialog(null, "Producto ya a�adido","ERROR",JOptionPane.ERROR_MESSAGE);
		} else {
			
			Ventana.modeloProductos.addElement(p);
			
		}
	}

	private void deleteProducto() {
		Producto p = (Producto) Ventana.listProductos.getSelectedValue();
		Ventana.modeloProductos.removeElement(p);
		
	}
	
	private void vaciarProducto() {
		Ventana.modeloProductos.removeAllElements(); 
	}
	
	private void change() {
		if (Ventana.btnVaciar_lista.isVisible()) {
			Ventana.btnVaciar_lista.setVisible(false);
			Ventana.btnDelete_lista.setVisible(false);
			Ventana.btnA�adir_lista.setVisible(false);
			Ventana.lbltextoProductos.setVisible(false);
			Ventana.btnVaciar.setVisible(true);
			Ventana.btnDelete.setVisible(true);
			Ventana.btnA�adir.setVisible(true);
			Ventana.lblTexto.setVisible(true);
		} else {
			Ventana.btnVaciar.setVisible(false);
			Ventana.btnDelete.setVisible(false);
			Ventana.btnA�adir.setVisible(false);
			Ventana.lblTexto.setVisible(false);
			Ventana.btnVaciar_lista.setVisible(true);
			Ventana.btnDelete_lista.setVisible(true);
			Ventana.btnA�adir_lista.setVisible(true);
			Ventana.lbltextoProductos.setVisible(true);
		}
	}
	
	private void calcularTotal() {
		BigDecimal total = new BigDecimal(0);
		for (int x=0 ; x < Ventana.modeloLista.getSize() ; x++) {
			Producto p = Ventana.modeloLista.getElementAt(x);
			total= total.add(new BigDecimal(p.precio));
			total = total.setScale(2, RoundingMode.DOWN);
		}
		Ventana.textTotal.setText(total+"�");
	}
}
