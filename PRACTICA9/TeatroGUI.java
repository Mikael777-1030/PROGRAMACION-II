import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TeatroGUI extends JFrame {
    private JRadioButton rbPalco, rbPlatea, rbGaleria;
    private JTextField tfNumero, tfDias;
    private JButton btnVender, btnSalir;
    private JLabel lblResultado;

    public TeatroGUI() {
        setTitle("Teatro Municipal");
        setSize(500, 360);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);
        setLocationRelativeTo(null); 

        setLayout(new BorderLayout(10, 10));

        
        JPanel panelTitulo = new JPanel(new BorderLayout());
        JLabel lblTitulo = new JLabel("Teatro Municipal", SwingConstants.CENTER);
        lblTitulo.setFont(new Font("Arial", Font.BOLD, 22));
        panelTitulo.add(lblTitulo, BorderLayout.CENTER);

        try {
            ImageIcon icono = new ImageIcon("teatro.jpg");
            Image img = icono.getImage().getScaledInstance(100, 60, Image.SCALE_SMOOTH);
            JLabel lblImagen = new JLabel(new ImageIcon(img));
            panelTitulo.add(lblImagen, BorderLayout.EAST);
        } catch (Exception ex) {
        
        }

        add(panelTitulo, BorderLayout.NORTH);

        
        JPanel panelCentro = new JPanel();
        panelCentro.setBorder(BorderFactory.createTitledBorder("Datos del Boleto"));
        panelCentro.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 10, 5, 10);
        gbc.fill = GridBagConstraints.HORIZONTAL;
        gbc.gridx = 0;
        gbc.gridy = 0;

        
        panelCentro.add(new JLabel("Tipo de entrada:"), gbc);

        gbc.gridx = 1;
        JPanel panelRadios = new JPanel(new FlowLayout(FlowLayout.LEFT));
        rbPalco = new JRadioButton("Palco");
        rbPlatea = new JRadioButton("Platea");
        rbGaleria = new JRadioButton("Galería");
        ButtonGroup grupo = new ButtonGroup();
        grupo.add(rbPalco);
        grupo.add(rbPlatea);
        grupo.add(rbGaleria);
        rbPalco.setSelected(true);
        panelRadios.add(rbPalco);
        panelRadios.add(rbPlatea);
        panelRadios.add(rbGaleria);
        panelCentro.add(panelRadios, gbc);

        
        gbc.gridx = 0;
        gbc.gridy++;
        panelCentro.add(new JLabel("Número:"), gbc);
        gbc.gridx = 1;
        tfNumero = new JTextField("1", 10);
        panelCentro.add(tfNumero, gbc);

        
        gbc.gridx = 0;
        gbc.gridy++;
        panelCentro.add(new JLabel("Cant. Días para el Evento:"), gbc);
        gbc.gridx = 1;
        tfDias = new JTextField("", 10);
        panelCentro.add(tfDias, gbc);

    
        gbc.gridx = 0;
        gbc.gridy++;
        btnVender = new JButton("Vende");
        panelCentro.add(btnVender, gbc);
        gbc.gridx = 1;
        btnSalir = new JButton("Salir");
        panelCentro.add(btnSalir, gbc);

        add(panelCentro, BorderLayout.CENTER);

    
        lblResultado = new JLabel(" ", SwingConstants.CENTER);
        lblResultado.setFont(new Font("Arial", Font.BOLD, 14));
        lblResultado.setForeground(Color.BLUE);
        lblResultado.setBorder(BorderFactory.createTitledBorder("Información"));
        add(lblResultado, BorderLayout.SOUTH);

        
        btnVender.addActionListener(e -> {
            try {
                int numero = Integer.parseInt(tfNumero.getText());
                int dias = tfDias.getText().isEmpty() ? 0 : Integer.parseInt(tfDias.getText());
                Boleto boleto;

                if (rbPalco.isSelected()) {
                    boleto = new Palco(numero);
                } else if (rbPlatea.isSelected()) {
                    boleto = new Platea(numero, dias);
                } else {
                    boleto = new Galeria(numero, dias);
                }

                lblResultado.setText(boleto.mostrarInformacion());
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Ingrese valores válidos.");
            }
        });

        btnSalir.addActionListener(e -> System.exit(0));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new TeatroGUI().setVisible(true));
    }
}
