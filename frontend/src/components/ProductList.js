import React from 'react';

function ProductList({ products }) {
  return (
    <div className="results-section">
      <h2>Products</h2>
      {products.length > 0 ? (
        <ul className="results-list product-list">
          {products.map((hit) => (
            <li key={hit._id} className="result-item product-item">
              <h4>{hit._source.product_title || 'Unnamed Product'}</h4>
              {/* Display refined content, fallback to original if needed */}
              <p>{hit._source.refined_content || hit._source.catalog_content || 'No description available.'}</p>
              <strong>Price: ${hit._source.price}</strong>
              <small>Size: {hit._source.size_value || 'N/A'} {hit._source.size_unit || ''}</small>
              <small>Relevance Score: {hit._score.toFixed(2)}</small>
            </li>
          ))}
        </ul>
      ) : (
        <p>No products found.</p>
      )}
    </div>
  );
}

export default ProductList;