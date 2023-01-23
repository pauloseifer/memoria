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

;; Cria buffer temporário, insere o conteúdo do bookmark, coloca o conteúdo das linhas
;; em que tem "site" em uma lista, lê o conteúdo da lista no buffer temp.json

(with-temp-buffer
  (insert-file-contents "~/repoprogs/site/bookmark.json")
  (goto-char (point-min))
  (cl-loop until (not (search-forward "site" nil "noerror"))
	do (push (thing-at-point 'line t) a))
  (with-current-buffer "temp.json"
    (erase-buffer)
    (while a
      (insert (car a))
      (setq a (cdr a)))
    )
)

;; Assim também funciona - notar a diferença no while
;; Por algum motivo o código todo em json é passado para *message* e não sei porquê

(with-temp-buffer
  (insert-file-contents "~/repoprogs/site/bookmark.json")
  (goto-char (point-min))
  ;;  (cl-loop until (not (search-forward "site" nil "noerror"))
  (while (search-forward "site" nil "noerror")
	(push (thing-at-point 'line t) a))
  (with-current-buffer "temp.json"
    (erase-buffer)
    (while a
      (insert (car a))
      (setq a (cdr a)))
    )
)
