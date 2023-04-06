%create a random string 
s = 'a':'z'; 
textString = ['start ' s(randi(26,1,10000)) ' end'];
 
%create figure 
hFig = figure(1); 
hFig.Units='normalized'; 
hFig.OuterPosition=[0 0 1 1];
 
%create panel 
hPan = uipanel('FontSize',12,... 
'BackgroundColor','white',... 
'Position',[0 0 1 1]); 
pos = getpixelposition(hPan);
 
%create textarea 
jTA = uicomponent('Parent',hPan,'style','javax.swing.jtextarea','tag','myObj',... 
'Text',textString,'Position',pos,'Units','pixels',... 
'BackgroundColor',[0.6 0.6 0.6],'Opaque',0,'LineWrap',1); 
jTA.Font = java.awt.Font('Helvetica', java.awt.Font.PLAIN, 22); % font name, style, size 
jTA.Foreground = java.awt.Color(1,1,1);
 
%attach scroll panel 
hSP = attachScrollPanelTo(jTA);
 
%resize figure to reveal vertical scrollbar
hFig.OuterPosition=[0 0 1 0.5];