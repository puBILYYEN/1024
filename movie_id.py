  doc = {
      "title": title,
      "picture": picture,
      "hyperlink": hyperlink,
      "showDate": showDate,
      "showLength": showLength,
      "lastUpdate": lastUpdate
  }

  db = firestore.client()
  doc_ref = db.collection("電影").document(movie_id)
  doc_ref.set(doc)
