;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(with-current-buffer "teste.txt"
  (insert "oi"))

(with-current-buffer "teste.txt"
  (dotimes (number 4)
    (insert "oi\n")))

(with-current-buffer "teste.txt"
  (goto-char (point-min))
    (dotimes (numero 4)
      (end-of-line)
      (insert (format "%i" numero))
      (next-line)
      ))
