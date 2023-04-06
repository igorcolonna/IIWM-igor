import java.awt.GraphicsConfiguration;

import java.awt.BorderLayout;

import java.awt.Label;

import javax.swing.JFrame;

import org.scijava.java3d.BranchGroup;
import org.scijava.java3d.Canvas3D;
import org.scijava.java3d.utils.geometry.ColorCube;
import org.scijava.java3d.utils.universe.SimpleUniverse;


public class CanvasDemo extends JFrame {

public CanvasDemo() {

   setLayout(new BorderLayout());
   Canvas3D canvas = new Canvas3D(null);

   add("North",new Label("This is the top"));

   add("Center", canvas);

   add("South",new Label("This is the bottom"));

   BranchGroup contents = new BranchGroup();

   contents.addChild(new ColorCube(0.3));

   SimpleUniverse universe = new SimpleUniverse(canvas);

   universe.getViewingPlatform().setNominalViewingTransform();

   universe.addBranchGraph(contents);

}

public static void main( String[] args ) {

   System.setProperty("sun.awt.noerasebackground", "true");

   CanvasDemo demo = new CanvasDemo();

   JFrame frame = new JFrame();
   frame.add(demo);
   frame.setVisible(true);
   
}

}