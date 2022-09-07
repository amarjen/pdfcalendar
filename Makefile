calendar: tex pdf clean

tex:
	@python3 ./calendar_tex.py --month $(MONTH) --year $(YEAR) > calendar.tex

pdf: 
	@pdflatex calendar.tex

clean:
	@rm *aux *log *tex

.PHONY: calendar tex pdf clean
