clear
% laminar boundaries according to Fig. 2 from Anderson & Linden 2009
% 
% First, measure the distance from WM to pia, and set this as 100%.
% Then, laminar thicknesses are:
% L1: 12.3%
% L2: 11.7%
% L3: 12.3%
% L4: 13.8%
% L5: 26.9%
% L6: 22.8%
% +- S.D. ~4%
% 
% and laminar center positions are:
% L1: 5.9%
% L2: 18.0%
% L3: 30.0%
% L4: 43.4%
% L5: 63.8%
% L6: 88.5%
% +- S.D. ~5%
% 
% A good rule of thumb is that L1-4 are roughly equal in thickness (~12.5%)
% and take up the top half of the cortex. L5-6 are also roughly equal
% (~25%) and take up the bottom half.

thickness(1)= 12.3;%
thickness(2)= 11.7;%
thickness(3)= 12.3;%
thickness(4)= 13.8;%
thickness(5)= 26.9;%
thickness(6)= 22.8;%

centers(1)= 5.9;%
centers(2)= 18.0;%
centers(3)= 30.0;%
centers(4)= 43.4;%
centers(5)= 63.8;%
centers(6)= 88.5;%

thickness
centers
boundaries=cumsum(thickness)/100

%cortical thickness varies quite a bit from mouse to mouse. You should
%really measure it for each section. But as a rough rule of thumb:
%in the 3 figures from Anderson & Linden 2009 showing photmicrographs of
%audtiory cortical sections, they are 794, 882, and 917 um thick, which is
%964 +/- 63 um
%for fixed tissue
%thus thickness in um is approximately
% L1: 119 um
% L2: 113 um
% L3: 119 um
% L4: 133 um
% L5: 259 um
% L6: 220 um
% +- S.D. 48 um 
% 
%and depth of the boundaries are round(boundaries*964) which are
round(boundaries*964);
% L1/L2: 119 um
% L2/L3: 231 um
% L3/L4 350 um
% L4/L5 483 um
% L5/L6 742 um
% L6/WM 964 um

fprintf('\nboundaries for 964 µm (Anderson fixed tissue):')
fprintf('\nL1/L2 %d\nL2/L3 %d\nL3/L4 %d\nL4/L5 %d\nL5/L6 %d\nL6/WM %d\n',round(boundaries*964))

fprintf('\nL1: %d-%d',0, round(boundaries(1)*964))
fprintf('\nL2: %d-%d',round([1 0]+boundaries(1:2)*964))
fprintf('\nL3: %d-%d',round([1 0]+boundaries(2:3)*964))
fprintf('\nL4: %d-%d',round([1 0]+boundaries(3:4)*964))
fprintf('\nL5: %d-%d',round([1 0]+boundaries(4:5)*964))
fprintf('\nL6: %d-%d',round([1 0]+boundaries(5:6)*964))

fprintf('\n_______________\n')

% for unfixed tissue, Instkirveli & Metherate 2012 measured total thickness
% to be 1045, so the depth of the boundaries are round(boundaries*1045) which are
round(boundaries*1045);
% L1/L2: 129 um
% L2/L3: 251 um
% L3/L4 379 um
% L4/L5 524 um
% L5/L6 805 um
% L6/WM 1045 um

fprintf('\nboundaries for 1045 µm (Metherate unfixed tissue):')
fprintf('\nL1/L2 %d\nL2/L3 %d\nL3/L4 %d\nL4/L5 %d\nL5/L6 %d\nL6/WM %d',round(boundaries*1045))
fprintf('\n')
fprintf('\nL1: %d-%d',0, round(boundaries(1)*1045))
fprintf('\nL2: %d-%d',round([1 0]+boundaries(1:2)*1045))
fprintf('\nL3: %d-%d',round([1 0]+boundaries(2:3)*1045))
fprintf('\nL4: %d-%d',round([1 0]+boundaries(3:4)*1045))
fprintf('\nL5: %d-%d',round([1 0]+boundaries(4:5)*1045))
fprintf('\nL6: %d-%d',round([1 0]+boundaries(5:6)*1045))

fprintf('\n\naligned to channels:')
fprintf('\nL1: %d-%d',0, 25*floor(boundaries(1)*1045/25))
fprintf('\nL2: %d-%d',25*(ceil(boundaries(1)*1045/25)),25*(floor(boundaries(2)*1045/25)))
fprintf('\nL3: %d-%d',25*(ceil(boundaries(2)*1045/25)),25*(floor(boundaries(3)*1045/25)))
fprintf('\nL3: %d-%d',25*(ceil(boundaries(3)*1045/25)),25*(floor(boundaries(4)*1045/25)))
fprintf('\nL3: %d-%d',25*(ceil(boundaries(4)*1045/25)),25*(floor(boundaries(5)*1045/25)))
fprintf('\nL3: %d-%d',25*(ceil(boundaries(5)*1045/25)),25*(floor(boundaries(6)*1045/25)))


% %just out of curiousity, if you use 
%     boundaries=[.125 .25 .375 .5 .75 1]
% fprintf('\nboundaries for 1045 µm (Metherate unfixed tissue):')
% fprintf('\nL1/L2 %d\nL2/L3 %d\nL3/L4 %d\nL4/L5 %d\nL5/L6 %d\nL6/WM %d\n',round(boundaries*1045))
% fprintf('\n')
% fprintf('\nL1: %d-%d',0, round(boundaries(1)*1045))
% fprintf('\nL2: %d-%d',round([1 0]+boundaries(1:2)*1045))
% fprintf('\nL3: %d-%d',round([1 0]+boundaries(2:3)*1045))
% fprintf('\nL4: %d-%d',round([1 0]+boundaries(3:4)*1045))
% fprintf('\nL5: %d-%d',round([1 0]+boundaries(4:5)*1045))
% fprintf('\nL6: %d-%d',round([1 0]+boundaries(5:6)*1045))
% 
% fprintf('\n_______________\nrounded to channels:')
% fprintf('\nL1: %d-%d',0, 25*round(round(boundaries(1)*1045)/25))
% fprintf('\nL2: %d-%d',25*([1 0]+round(round(boundaries(1:2)*1045)/25)))
% fprintf('\nL3: %d-%d',25*([1 0]+round(round([1 0]+boundaries(2:3)*1045)/25)))
% fprintf('\nL4: %d-%d',25*([1 0]+round(round([1 0]+boundaries(3:4)*1045)/25)))
% fprintf('\nL5: %d-%d',25*([1 0]+round(round([1 0]+boundaries(4:5)*1045)/25)))
% fprintf('\nL6: %d-%d',25*([1 0]+round(round([1 0]+boundaries(5:6)*1045)/25)))
% 

figure; hold on
lbx=repmat(boundaries*1045, 2, 1);
lby=ones(size(lbx));
lby(1,:)=-1;
L=line(lby, lbx);
set(L, 'color', 'r', 'linewid', 2)
ch=0:25:1100;
plot( 0,ch, '*')
set(gca, 'ytick', ch)
grid on
text(-.5, 50, 'L1')
text(-.5, 200, 'L2')
text(-.5, 300, 'L3')
text(-.5, 450, 'L4')
text(-.5, 700, 'L5')
text(-.5, 950, 'L6')
title('25 µm channels aligned to 400 µm with total depth of 1045 µm')

